#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 4
Title: follow the chain
http://www.pythonchallenge.com/pc/def/linkedlist.php

image: web/site/chainsaw.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

In the page source:

    <!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never
    end. 400 times is more than enough. -->
    <center>
    <a href="linkedlist.php?nothing=12345">
        <img src="chainsaw.jpg" border="0"/>
    </a>

"""

import os
import re
import sys
import urllib


def get_number(text, previous=0):
    regex = re.compile('nothing(?:=|\sis\s)(\d{3,5})')
    result = regex.search(text)
    try:
        return result.groups()[0]
    except:
        if text == 'Yes. Divide by two and keep going.':
            return str(int(previous) / 2)
        return False

pcurl = 'http://www.pythonchallenge.com/pc/def/'

url_original = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

url_4_links = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

page = urllib.urlopen(url_original).read()
number = get_number(page)
url_to_follow = url_4_links + number
output = [{'url': url_original, 'number': number, 'page': page}]

for i in xrange(0, 300):
    page = urllib.urlopen(url_to_follow).read()
    number = get_number(page, number)
    if number:
        output += [{'url': url_to_follow, 'number': number, 'page': page}]
        url_to_follow = url_4_links + number
    else:
        print 'Error capturing data in:\n'
        print url_to_follow
        print page
        print os.linesep
        print 'Previous link:'
        last_link = output[len(output) - 1]
        print last_link['url']
        print last_link['number']
        print last_link['page']
        print os.linesep * 2
        print "The next url is {0}{1}.html".format(pcurl, page)
        sys.exit()
