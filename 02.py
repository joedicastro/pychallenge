#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Python Challenge
Level 2
Title: ocr
http://www.pythonchallenge.com/pc/def/ocr.html

image: web/site/ocr.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

message:

    recognize the characters. maybe they are in the book,
    but MAYBE they are in the page source.

"""

import re
import urllib2

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
pcurl = 'http://www.pythonchallenge.com/pc/def/'

page = urllib2.urlopen(url)
content = page.read()

extract_text = re.compile('<!--\n(.*?)\n-->', re.DOTALL)
text_to_recognize = re.findall(extract_text, content)[1]

recognize_chars = re.compile('[a-zA-Z0-9]')
recognized_chars = ''.join(re.findall(recognize_chars, text_to_recognize))

print 'The next url is {0}{1}.html'.format(pcurl, recognized_chars)
