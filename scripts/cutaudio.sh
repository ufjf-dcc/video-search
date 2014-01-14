#!/bin/bash

#extrai audio do video (mp4) para wav
ffmpeg -i $1.mp4 -vn -ac 1 -ab 160k -ar 22050 $1.wav

#pega tamanho total do audio em segundos
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

#remove silêncio dos arquivos cortados
for f in $1_[0-9]*.wav
do
	sox $f sil$f silence 1 0.1 1% -1 0.5 1%
done

mkdir transc
for j in sil*.wav
do
	if [[ $(soxi -D $j) > 60 ]]
	then
		python ../spk_drztn.py $j
		#move todos os audios segmentados de todos os clusters para a pasta transc
		find ./${j%.*}/S* -type f -name '*.wav' -exec rename "s/S[0-9]*_/${j%.*}_/" {} \;
		find ./${j%.*}/S* -iname '*.wav' -exec mv {} transc \;
		rm -r ./${j%.*}/ #remove as pastas vazias dos clusters
	else
		mv $j transc
	fi
done
