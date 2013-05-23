#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 11
Title: odd even
http://www.pythonchallenge.com/pc/return/5808.html

image: web/site/cave.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

The only hint is the image

"""


import base64
import Image
import ImageEnhance
import urllib2

pcurl = 'http://www.pythonchallenge.com/pc/return/'
img_url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'

request = urllib2.Request(img_url)
base64string = base64.encodestring('{0}:{1}'.format('huge',
                                                    'file')).replace('\n', '')
request.add_header("Authorization", "Basic {0}".format(base64string))
img = urllib2.urlopen(request)
with open('cave.jpg', 'wb') as img_file:
    img_file.write(img.read())

image = Image.open('cave.jpg')

for x in xrange(image.size[0]):
    for y in xrange(image.size[1]):
        if (x + y) % 2 != 0:
            image.putpixel((x, y), (0, 0, 0))

bright = ImageEnhance.Brightness(image)
image = bright.enhance(2.5)
contrast = ImageEnhance.Contrast(image)
image = contrast.enhance(3.0)
image.show()
image.save('cave.png')

# the image shows the word 'evil'
print "The next url is {0}{1}.html".format(pcurl, 'evil')
