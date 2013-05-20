#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 6
Title: now there are pairs
http://www.pythonchallenge.com/pc/def/channel.html

image: web/site/channel.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

in the html source:

    <!-- <-- zip -->

"""

import re
import urllib
import zipfile

pcurl = 'http://www.pythonchallenge.com/pc/def/'
url = 'http://www.pythonchallenge.com/pc/def/channel.html'
zip_url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
page = urllib.urlopen(url).read()

zip_file = urllib.urlretrieve(zip_url)[0]
zipfile = zipfile.ZipFile(zip_file)

# zipfile.printdir()
total_files = len(zipfile.namelist())

# print zipfile.read('readme.txt')

# content of readme.txt
# welcome to my zipped list.
#
# hint1: start from 90052
# hint2: answer is inside the zip

# print zipfile.read('90052.txt')

# content of 90052.txt
# Next nothing is 94191

regex = re.compile('nothing is (\d*)')

text = zipfile.read('90052.txt')
next_file = regex.search(text).groups()[0]

comments = ''
for i in xrange(0, total_files):
    text = zipfile.read(next_file + '.txt')
    info = zipfile.getinfo(next_file + '.txt')
    comments += info.comment
    try:
        next_file = regex.search(text).groups()[0]
    except:
        print '{0} of {1}: {2}.txt'.format(i, total_files, next_file)
        print text + '\n'
        break
        # output of 46145.txt:
        # Collect the comments.

print comments

# output of comments:

# ***************************************************************
# ****************************************************************
# **                                                            **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
# **                                                            **
# ****************************************************************
#  **************************************************************


print "The next url is {0}{1}.html".format(pcurl, 'oxygen')
