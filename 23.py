#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 23
Title: what is this module?
http://www.pythonchallenge.com/pc/hex/bonus.html

image_file: web/site/bonus.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

in the html source code:

    <!--
    TODO: do you owe someone an apology? now it is a good time to
    tell him that you are sorry. Please show good manners although
    it has nothing to do with this level.
    -->

    <!-- 	it can't find it. this is an undocumented module. -->

    <!--
    'va gur snpr bs jung?'
    -->

"""

# if we send a mail to Mr. leopold saying Sorry, he answers this:
#
#   Never mind that.
#
#   Have you found my broken zip?
#
#   md5: bbb8b499a0eef99b52c7f13f4e78c24b
#
#   Can you believe what one mistake can lead to?
#


import base64
import re
import urllib2

pcurl = 'http://www.pythonchallenge.com/pc/hex/'
url = 'http://www.pythonchallenge.com/pc/hex/bonus.html'

request = urllib2.Request(url)
authorization = base64.b64encode('{0}:{1}'.format('butter', 'fly'))
request.add_header("Authorization", "Basic {0}".format(authorization))
page = urllib2.urlopen(request).read()


# the real hint is this:
#
#   this is an undocumented module.
#
# which refers to the Zen of Python by Tim Peters
#
# if we get the code of the module (this not mine, is Tim Peter's code) we can
# solve the second hint as encrypted question
extract_hint = re.compile("<!--\n'(.*)'\n-->", re.DOTALL | re.MULTILINE)
s = re.search(extract_hint, page).group(1)

print s
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i + c)] = chr((i + 13) % 26 + c)

print "".join([d.get(c, c) for c in s])

# in the face of what?, if we read the Zen of Python, is 'ambiguity'
print "\nThe next url is {0}{1}.html".format(pcurl, 'ambiguity')
