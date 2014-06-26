# -*- coding: utf-8 -*-
'''
Created on June 16, 2014

@author: hygor
'''

import codecs
import collections
import os
from random import randint

rulesFile = codecs.open('g2p_table.txt', 'r', encoding='utf8')  # arquivo com representações fonéticas de cada letra
wordsFile = codecs.open('words.txt', 'r', encoding='utf8')  # arquivo com lista de palavras a serem utilizadas no dicionário (uma palavra por linha)
tempDic = codecs.open('temp_dict.dic', 'w+', encoding='utf8')  # arquivo com dicionário sem remoção de repetições
resultDic = codecs.open('dictionary.dic', 'w', encoding='utf8')  # arquivo onde será escrito o dicionário

# inserção das representações fonéticas em uma estrutura de dicionário
dic = collections.defaultdict(list)
for line in rulesFile:
    dic[line[0]].append(line[2:])

dicFirstPos = tempDic.tell()
tempDic.write("</s> [] sil\n")
tempDic.write("<s> [] sil\n")
# geração das representações fonéticas de cada palavra contida em words.txt
for word in wordsFile:
    word = word.strip()
    i = 0
    while i < 5:
        x = ''
        for char in word:
            x += dic[char][randint(0, len(dic[char]) - 1)]
            y = ''.join(x).splitlines()
            y = ' '.join(y)
        tempDic.write(word + '    ' + y + '  ' + '\n')
        i += 1

tempDic.seek(dicFirstPos)
# remove linhas repetidas no dicionário
seen = set()
for line in tempDic:
    if line not in seen:
        seen.add(line)
resultDic.writelines(sorted(seen))

rulesFile.close()
wordsFile.close()
tempDic.close()
resultDic.close()
os.remove('temp_dict.dic')

print 'Dicionário gerado em dictionary.dic'
