# -*- coding: utf-8 -*-
'''
Created on Apr 16, 2014

@author: hygor
'''

import codecs
import collections
from itertools import product

rulesFile = codecs.open('g2p_table.txt', 'r', encoding='utf8') #arquivo com representações fonéticas de cada letra
wordsFile = codecs.open('words.txt', 'r', encoding='utf8') #arquivo com lista de palavras a serem utilizadas no dicionário (uma palavra por linha)
resultDic = codecs.open('dictionary.dic', 'w', encoding='utf8') #arquivo onde será escrito o dicionário

#inserção das representações fonéticas em uma estrutura de dicionário
dic = collections.defaultdict(list)
for line in rulesFile:
    dic[line[0]].append(line[2:])

resultDic.write("</s> [] sil\n")
resultDic.write("<s> [] sil\n")
#geração de todas as representações fonéticas de cada palavra contida em words.txt
for word in wordsFile:
    word = word.strip()
    for x in product(*(dic[char] for char in word)):
        y = ' '.join(x).splitlines()
        y = ''.join(y)        
        resultDic.write(word + '    ' + y + '\n' )

rulesFile.close()
wordsFile.close()
resultDic.close()
