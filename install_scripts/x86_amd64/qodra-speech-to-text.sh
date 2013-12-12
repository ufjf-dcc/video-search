#!/bin/bash
#+--------------------------------------------------------------+
#| QODRA	 - Download script / Speech-to-text script	|
#|                 for raspberry                                |
#|                                                              |
#| sandro.coelho@ice.ufjf.br					|
#+--------------------------------------------------------------+

echo 'downloading unrar package...'
apt-get install unrar

echo 'downloading Julius(speech-to-text tool)...'
wget https://dl.dropboxusercontent.com/u/161746017/julius_coruja/v0.1/julius/julius-4.2.3.tar.gz


echo 'downloading Coruja Portuguese language files -  provided by UFPA...'
wget https://dl.dropboxusercontent.com/u/161746017/julius_coruja/v0.1/lm_dic/coruja_jlapsapi1.5.rar
wget https://dl.dropboxusercontent.com/u/161746017/julius_coruja/v0.1/lm_dic/dictionary_ssp.dic

echo 'downloading config files...'
wget https://dl.dropboxusercontent.com/u/161746017/julius_coruja/v0.1/config/julius.jconf


echo 'downloading sample files...'
wget https://dl.dropboxusercontent.com/u/161746017/julius_coruja/v0.1/example/lista
wget https://dl.dropboxusercontent.com/u/161746017/julius_coruja/v0.1/example/voz_do_brasil_09_12_2013.wav

echo 'unpacking julius...'
tar xvf julius-4.2.3.tar.gz

echo 'unpacking Coruja Portuguese language files...'
unrar e coruja_jlapsapi1.5.rar

echo 'installing julius...'
cd julius-4.2.3/
./configure
make
make install
cd ..

echo 'creating folders...'
mkdir /usr/local/bin/pt_BR/
mkdir /usr/local/bin/pt_BR/sample

echo 'installing language files...'
cd coruja_jlapsapi
mv * /usr/local/bin/pt_BR/
cd ..
rm coruja_jlapsapi -r
mv dictionary_ssp.dic /usr/local/bin/pt_BR/

echo 'installing config files...'
rm /usr/local/bin/julius.jconf
mv julius.jconf /usr/local/bin/pt_BR/


echo 'installing sample files...'
mv lista /usr/local/bin/pt_BR/
mv voz_do_brasil_09_12_2013.wav /usr/local/bin/pt_BR/sample



