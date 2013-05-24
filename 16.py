#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 16
Title: let me get this straight
http://www.pythonchallenge.com/pc/return/mozart.html

image: web/site/mozart.gif


###############################################################################
#                                    Hint                                     #
###############################################################################

The only hint is the image

"""


import base64
from collections import deque
import Image
import urllib2
from cStringIO import StringIO


pcurl = 'http://www.pythonchallenge.com/pc/return/'
img_url = 'http://www.pythonchallenge.com/pc/return/mozart.gif'

request = urllib2.Request(img_url)
base64string = base64.encodestring('{0}:{1}'.format('huge',
                                                    'file')).replace('\n', '')
request.add_header("Authorization", "Basic {0}".format(base64string))
img = urllib2.urlopen(request).read()

image = Image.open(StringIO(img))
pixels = list(image.getdata())

# the image seems to have the pixels zigzagged in some way. Also there is a
# common pattern in all the lines, a serie of 1 white + 4 pink + 1 white
# pixels. Let's use this pattern to align all the lines.
for y in xrange(image.size[1]):
    line = pixels[image.size[0] * y: image.size[0] * (y + 1)]
    idx = line.index(195) + 3  # where is the first pink pixel
    straight_line = deque(line)
    straight_line.rotate(image.size[0] - idx)
    for x in xrange(image.size[0]):
        image.putpixel((x, y), straight_line[x])

image.show()
image.save('mozart_straight.gif')

# the image shows the word 'romance'
print "The next url is {0}{1}.html".format(pcurl, 'romance')
