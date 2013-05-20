#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 5
Title: peak hell
http://www.pythonchallenge.com/pc/def/peak.html

image: web/site/peakhell.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

message:

    pronounce it

in the html source:

    <peakhell src="banner.p"/>

"""


import pickle
import re
import urllib

pcurl = 'http://www.pythonchallenge.com/pc/def/'
url = 'http://www.pythonchallenge.com/pc/def/peak.html'

page = urllib.urlopen(url).read()

# we get the file "banner.p"
regex = re.compile('peakhell src="(.*)"')
pickle_file = regex.search(page).groups()[0]
pickle_url = pcurl + pickle_file

# the banner.p file is a pickle object
pickle_object = pickle.loads(urllib.urlopen(pickle_url).read())

for e in pickle_object:
    line = ''
    for i in e:
        line += i[1] * i[0]
    print line

# the banner says: channel

print 'The next url is {0}{1}.html'.format(pcurl, 'channel')
