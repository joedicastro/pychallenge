#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 8
Title: working hard?
http://www.pythonchallenge.com/pc/def/integrity.html

image: web/site/integrity.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

message:

    Where is the missing link?

in the html source:

  The bee in the image is linked to:

        href="../return/good.html"

  At the end there is this comment:

    <!--
    un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00
    \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$
    \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    -->

  If we follow the link, we are asked for an user and a password whith this
  message:

      inflate

"""


import bz2
import re
import urllib2

pcurl = 'http://www.pythonchallenge.com/pc/return/'
url = 'http://www.pythonchallenge.com/pc/def/integrity.html'

page = urllib2.urlopen(url)
content = page.read()

# The hints suggests that 'un' and 'pw' are the username and password
# respectively. The message inflate suggest decompression and the first two
# chars of each field the BZip2 format.
extract_user = re.compile(r"un: '(.*)'")
extract_password = re.compile(r"pw: '(.*)'")

username = re.findall(extract_user, content)[0].decode('string_escape')
password = re.findall(extract_password, content)[0].decode('string_escape')

print "The next url is {0}{1}.html".format(pcurl, 'good')

print ("The username is '{0}' and the password is '{1}'".
       format(bz2.decompress(username), bz2.decompress(password)))
