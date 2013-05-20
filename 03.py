#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Python Challange
Level 3
Title: re
http://www.pythonchallenge.com/pc/def/equality.html

image: web/site/bodyguard.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

message:

     One small letter, surrounded by EXACTLY three big bodyguards on each of
     its sides.

"""

import re
import urllib2

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
pcurl = 'http://www.pythonchallenge.com/pc/def/'


page = urllib2.urlopen(url)
content = page.read()

extract_text = re.compile('<!--\n(.*?)\n-->', re.DOTALL)
text_to_recognize = extract_text.search(content).groups()[0]

regex = re.compile('[a-z]{1}[A-Z]{3}([a-z]){1}[A-Z]{3}[a-z]{1}')
result = re.findall(regex, text_to_recognize)

print 'The next url is {0}{1}.html'.format(pcurl, ''.join(result))
