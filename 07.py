#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Python Challenge
Level 7
Title: smarty
http://www.pythonchallenge.com/pc/def/oxygen.html

image: web/site/oxygen.png


###############################################################################
#                                    Hint                                     #
###############################################################################

The image is the hint, it shows a grey bar in the middle, probably the key.

"""

import urllib
import Image

pcurl = 'http://www.pythonchallenge.com/pc/def/'

img_url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'

img_file = urllib.urlretrieve(img_url)[0]
image = Image.open(img_file)

print ("The image have {0} format and a size of {1}x{2} pixels in {3} mode.\n".
       format(image.format, image.size[0], image.size[1], image.mode))

# we need to decode the grey bar. Grey pixels in RGBA mode have three equal
# values for R, G & B. The alpha (A) value doesn't matter.
# first find where the bar starts vertically
for y in xrange(image.size[1]):
    if len(set(image.getpixel((0, y)))) == 2:
        break

# now, find where it ends horizontally
for x in xrange(image.size[0]):
    if len(set(image.getpixel((x, y)))) != 2:
        break

# if we walk all the grey bar's pixels horizontally, assuming that each color
# level is an ASCII code, we can see a text that repeats each char 7 times
text = ''.join(chr(image.getpixel((i, y))[0]) for i in xrange(0, x, 7))
print 'The text inside the grey bar is:\n\n{0}\n'.format(text)

# the last part of the text is a list, assuming they are ASCII chars too:
key = ''.join(chr(int(c)) for c in text.split('[')[1].split(']')[0].split(','))

print "The next url is {0}{1}.html".format(pcurl, key)
