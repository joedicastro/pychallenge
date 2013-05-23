#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 14
Title: walk around
http://www.pythonchallenge.com/pc/return/disproportional.html

image: web/site/italy.jpg
image: web/site/wire.png


###############################################################################
#                                    Hint                                     #
###############################################################################

in the html source:

    <!-- remember: 100*100 = (100+99+99+98) + (...  -->

and there is an additional image, 'wire.png' that is a 10000x1 image_pixels
PNG, but is showed like a 100x100 image_pixels image

"""

import base64
import urllib2
import Image
from cStringIO import StringIO


def spiral(pixels):
    length = int(len(pixels) ** 0.5)
    matrix = [[0 for i in xrange(length)] for j in xrange(length)]
    matrix[0] = [pixels[i] for i in xrange(length)]
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    direction, row, col, idx = 0, 0, length - 1, length
    for line in xrange(length - 1, 0, -1):
        for iteration in xrange(2):
            for position in xrange(line, 0, -1):
                row += directions[direction][0]
                col += directions[direction][1]
                matrix[row][col] = pixels[idx]
                idx += 1
            direction += 1
            if direction == 4:
                direction = 0
    return matrix


pcurl = 'http://www.pythonchallenge.com/pc/return/'
img_url = 'http://www.pythonchallenge.com/pc/return/wire.png'

request = urllib2.Request(img_url)
base64string = base64.encodestring('{0}:{1}'.format('huge',
                                                    'file')).replace('\n', '')
request.add_header("Authorization", "Basic {0}".format(base64string))
img = urllib2.urlopen(request).read()

# the main image, the dimensions of the second one and the hint suggests that
# the goal is to "bend" the wire into a spiral
image = Image.open(StringIO(img))
image_pixels = image.getdata()

# let's twist the original pixels from "wire.png"
spiral_pixels = spiral(image_pixels)

# now we create a new image with this spiral structure
new = Image.new('RGB', (100, 100))

for x in xrange(100):
    for y in xrange(100):
        new.putpixel((x, y), spiral_pixels[y][x])
new.save('wire_spiral.png')
new.show()

# the image shows a cat, and if we go to the 'cat.html' url we have another
# page with a greater picture of the same cat with a "colleague" and this
# message:
#
#    and its name is uzi. you'll hear from him later.

print "The next url is {0}{1}.html".format(pcurl, 'uzi')
