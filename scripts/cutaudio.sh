#!/bin/bash

#pega tamanho total do audio em segundos
FILE_LENGTH=$(sox $1.mp3 -n stat 2>&1 | sed -n 's#^Length (seconds):[^0-9]*\([0-9.]*\)$#\1#p')
var=$(echo $FILE_LENGTH|awk '{print int($1+0.5)}')


#preenche um array com os tempos de 0 até o tamanho do audio
array=( 0 $(grep -o '<time>[0-9].*</time>' $1.index.xml | sed 's/\(<time>\|<\/time>\)//g') $var )

#corta o audio
for (( i = 0; i < ${#array[@]}; i++ ))
do
	e=`expr ${array[i+1]} - ${array[i]}`
	ffmpeg -ss ${array[i]} -t $e -i $1.mp3 -acodec copy $1_$i.mp3
done
