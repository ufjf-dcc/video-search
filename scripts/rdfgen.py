'''
Created on Apr 9, 2014

@author: hygor
'''

import xml.etree.ElementTree as ET
import re
import sys

#para executar: python rdfgen.py <nome do arquivo xml sem extensao>
tree1 = ET.parse(sys.argv[1] + '.xml')
root = tree1.getroot()

TITLE = root.find('general/title/string').text
#ABSTRACT = root.find('').text
DATE = root.find('lifecycle/contribute/date').text
COURSENAME = root.find('videoaula/educational/course/title/string').text
COURSECODE = root.find('videoaula/educational/course/code').text
KEYWORDS = root.find('general/keyword/string').text
TAXONOMY = root.find('classification/taxonPath/taxon/entry/string').text
#REFERENCES = root.find('').text
DESCRIPTION = root.find('general/description/string').text
c = 1
for creator in root.findall('lifecycle/contribute'):
    d = creator.find('entity').text
    d = re.sub('^%s' % '(BEGIN:VCARD\\\\nFN:)', '', d)
    d = re.sub('%s$' % '(END:VCARD\\\\n)', '', d)
    if c == 1:
        PUBLISHER = d
    elif c == 2:
        CREATOR = d
    c += 1
#LICENSE = root.find('').text
LANGUAGE = root.find('general/language').text
#EDUCATIONLEVEL = root.find('').text
ENTRY = root.find('general/identifier/entry').text

f = open(sys.argv[1] + '_rdf.txt', 'w')
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/title",TITLE.encode('utf-8')))
#f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/abstract",ABSTRACT.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\"^^xsd:date .\n" %(ENTRY,"http://purl.org/dc/terms/date",DATE.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/coursename",COURSENAME.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/coursecode",COURSECODE.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/keywords",KEYWORDS.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/taxonomy",TAXONOMY.encode('utf-8')))
#f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/references",REFERENCES.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/description",DESCRIPTION.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/publisher",PUBLISHER.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/creator",CREATOR.encode('utf-8')))
#f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/license",LICENSE.encode('utf-8')))
f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/language",LANGUAGE.encode('utf-8')))
#f.write("<%s>\t<%s>\t\"%s\" .\n" %(ENTRY,"http://purl.org/dc/terms/educationlevel",EDUCATIONLEVEL.encode('utf-8')))
f.close()
