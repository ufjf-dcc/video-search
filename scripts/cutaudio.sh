#!/bin/bash

#extrai audio do video (mp4) para wav
ffmpeg -i $1.mp4 -vn -ac 1 -ab 160k -ar 16000 $1.wav

#pega tamanho total do audio em segundos
#FILE_LENGTH=$(sox $1.wav -n stat 2>&1 | sed -n 's#^Length (seconds):[^0-9]*\([0-9.]*\)$#\1#p')
FILE_LENGTH=$(soxi -D $1.wav)
var=$(echo $FILE_LENGTH|awk '{print int($1+0.5)}')


#preenche um array com os tempos de 0 até o tamanho do audio
array=( 0 $(grep -o '<time>[0-9].*</time>' $1.index.xml | sed 's/\(<time>\|<\/time>\)//g') $var )

#corta o audio
for (( i = 0; i < ${#array[@]}; i++ ))
do
	if [[ i -eq 0 && ${array[1]} -eq 0 ]];
	then
		i=$[i+1]
	fi
	e=`expr ${array[i+1]} - ${array[i]}`
	ffmpeg -ss ${array[i]} -t $e -i $1.wav -acodec copy $1_$i.wav
done

#remove silêncio dos arquivos cortados, normalize e compand
for f in $1_[0-9]*.wav
do
	cp $f speech_$f
	normalize-audio speech_$f
	sox speech_$f edited_$f compand 0.03,1 -90,-90,-70,-70,-60,-45,0,0 -5
	sox edited_$f sil$f silence 1 0.1 1% -1 0.5 1%
	rm speech_$f
	rm edited_$f
done

#cria a pasta transc para armazenar os áudios que serão usados para transcrição
mkdir transc 
for j in sil*.wav
do
	if [[ "$(echo $(soxi -D $j)|awk '{print int($1+0.5)}')" -gt "45" ]] #caso o áudio tenha mais que 45seg faz a diarização
	then
		#faz a diarização
		python ../spk_drztn.py $j
		#move todos os audios segmentados de todos os clusters para a pasta transc
		find ./${j%.*}/S* -type f -name '*.wav' -exec rename "s/S[0-9]*_/${j%.*}_/" {} \;
		find ./${j%.*}/S* -iname '*.wav' -exec mv {} transc \;
		#remove as pastas vazias dos clusters
		rm -r ./${j%.*}/
	else #se não apenas move o áudio para transc
		mv $j transc
	fi
done

cd transc
#copia o caminho dos áudios a serem transcritos para o arquivo lista do julius
for f in *.wav
do
	echo "$(readlink -f $f)"
done > /usr/local/bin/pt_br/1.7/lista
#faz a transcrição
julius -C /usr/local/bin/pt_BR/1.7/julius.jconf | grep pass1_best: > transcrito.txt
#remove 'pass1_best:' do arquivo transcrito
sed -i 's/pass1_best:  //' transcrito.txt
