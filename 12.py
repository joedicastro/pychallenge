#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 12
Title: dealing evil
http://www.pythonchallenge.com/pc/return/evil.html

image: web/site/evil1.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

The only hint is the image name. The name evil1 suggest that could be another
file named evil2.jpg and so on.

In fact, there is an evil2.jpg image file that says:

    not
    jpg -
    - .gfx

The file evil2.gfx seems to be the gfx_file to resolve this level.

There is another evil3.jpg file that says:

    no
    more
    evils...

And a final evil4.jpg file that in fact is a text file that says:

    Bert is evil! go back!

"""


import base64
import imghdr
import urllib2
from cStringIO import StringIO

pcurl = 'http://www.pythonchallenge.com/pc/return/'
img_url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'

request = urllib2.Request(img_url)
base64string = base64.encodestring('{0}:{1}'.format('huge',
                                                    'file')).replace('\n', '')
request.add_header("Authorization", "Basic {0}".format(base64string))
img = urllib2.urlopen(request)
with open('evil2.gfx', 'wb') as img_file:
    img_file.write(img.read())

# if we take a look to the gfx file header:
gfx_file = open('evil2.gfx', 'rb').read()
print "The .gfx file's header:\n"
print ' '.join(['{0:02X}'.format(ord(char)) for char in gfx_file[:15]])
print

# We can se this:
# FF 89 47 89 FF D8 50 49 50 D8 FF 4E 46 4E FF
#
# These are various file magic numbers (signature) for some image file formats:
#
# GIF (87a):    47 49 46 38 37 61
# JPEG:         FF D8
# PNG:          89 50 4E 47 0D 0A 1A 0A
#
# Now let's take a closer look to the .gfx's header:
#
# FF 1ˢᵗ byte of JPEG signature
# 89 1ˢᵗ byte of PNG signature
# 47 1ˢᵗ byte of GIF signature
# 89 1ˢᵗ byte of PNG signature
# FF 1ˢᵗ byte of JPEG signature
# -------------------------------
# D8 2ⁿᵈ byte of JPEG signature
# 50 2ⁿᵈ byte of PNG signature
# 49 2ⁿᵈ byte of GIF signature
# 50 2ⁿᵈ byte of PNG signature
# D8 2ⁿᵈ byte of JPEG signature
# -------------------------------
# FF 1ˢᵗ byte of data of a JPEG file
# 4E 3ʳᵈ byte of PNG signature
# 46 3ʳᵈ byte of GIF signature
# 4E 3ʳᵈ byte of PNG signature
# FF 1ˢᵗ byte of data of a JPEG file
# ...
#
# So, seems clear to me that we have 5 images multiplexed in one file.

hidden_images = {n: '' for n in xrange(5)}

for i in xrange(5):
    hidden_images[i] = gfx_file[i::5]

filetype = {0: 'jpeg', 1: 'png', 2: 'gif', 3: 'png', 4: 'jpeg'}

for image, raw_data in hidden_images.items():
    if imghdr.what(StringIO(raw_data)) in ('jpeg', 'png', 'gif'):
        filename = 'evil_hidden_{0}.{1}'.  format(image, filetype[image])
        with open(filename, 'wb') as out:
            out.write(raw_data)

# the word in the images is 'disproportional'
print "The next img_url is {0}{1}.html".format(pcurl, 'disproportional')
