# -*- coding: utf-8 -*-
'''
Created on Apr 9, 2014

@author: hygor
'''

import xml.etree.ElementTree as ET
import re
import sys
import os
import codecs

fileName, fileExtension = os.path.splitext(sys.argv[1])

tree = ET.parse(fileName + fileExtension)
root = tree.getroot()

TITLE = root.find('general/title/string').text
#ABSTRACT = root.find('').text
DATE = root.find('lifecycle/contribute/date').text
#REFERENCES = root.find('').text
with codecs.open("transcrito_" + fileName + ".txt", "r", encoding='utf8') as transcrito:
    DESCRIPTION = transcrito.read().replace('\n', ' ')
COURSENAME = root.find('videoaula/educational/course/title/string').text
COURSECODE = root.find('videoaula/educational/course/code').text
KEYWORDS = root.find('general/keyword/string').text
c = 1
for creator in root.findall('lifecycle/contribute'):
    d = creator.find('entity').text
    d = re.sub('^%s' % '(BEGIN:VCARD\\\\nFN:)', '', d)
    d = re.sub('%s$' % '(END:VCARD\\\\n)', '', d)
    if c == 1:
        PUBLISHER = d
    elif c == 2:
        CREATOR = d.rstrip()
    c += 1
#LICENSE = root.find('').text
LANGUAGE = root.find('general/language').text
#EDUCATIONLEVEL = root.find('').text
if root.find('general/identifier/entry') != None:
    ENTRY = root.find('general/identifier/entry').text
else:
	ENTRY = ''

f = open(fileName + '_rdf.txt', 'w')
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/title",TITLE.encode('utf-8')))
#f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/abstract",ABSTRACT.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\"^^xsd:date .\n" %(ENTRY,"http://purl.org/dc/terms/date",DATE.encode('utf-8')))
#f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/references",REFERENCES.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/description",DESCRIPTION.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/publisher",PUBLISHER.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/creator",CREATOR.encode('utf-8')))
#f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/license",LICENSE.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/language",LANGUAGE.encode('utf-8')))
#f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/educationlevel",EDUCATIONLEVEL.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/coursename",COURSENAME.encode('utf-8')))
if COURSECODE != None:
	f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/coursecode",COURSECODE.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/keywords",KEYWORDS.encode('utf-8')))
f.close()
