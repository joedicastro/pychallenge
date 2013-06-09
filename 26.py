#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 26
Title: be a man - apologize!
http://www.pythonchallenge.com/pc/hex/decent.html

image_file: web/site/decent.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

message:

    Hurry up, I'm missing the boat

in the html source:

    <!-- you've got his e-mail -->

"""

# the title and the hint in the html source refers to a previous email that I
# sent to Mr. Leopold in level 23.
# His answer was:
#
# Never mind that.
#
# Have you found my broken zip?
# md5: bbb8b499a0eef99b52c7f13f4e78c24b
#
# Can you believe what one mistake can lead to?
#
# and I found the 'mybroken.zip' in level 24

import hashlib
import Image
import zipfile
from cStringIO import StringIO

pcurl = 'http://www.pythonchallenge.com/pc/hex/'

broken_zip = zipfile.ZipFile('mybroken.zip')
# the zip file has an image inside
print 'The content of the zip file is "{0}"'.format(broken_zip.namelist()[0])
# the zip seems to be broken
print 'The file "{0}" is broken (Bad CRC).'.format(broken_zip.testzip())
# we're going to extract it anyway
gif_zipinfo = broken_zip.getinfo('mybroken.gif')
gif_zipinfo.CRC = None
broken_zip.extract(gif_zipinfo)
broken_gif = Image.open('mybroken.gif')
try:
    broken_gif.show()
except IOError:
    print "It's true, the image is broken."

# So, we have a broken zip, and a right md5 hash, in fact, the current hash
# doesn't match with the one given by Mr. L.
broken_zip_str = open('mybroken.zip', 'r').read()
right_hash = 'bbb8b499a0eef99b52c7f13f4e78c24b'
if right_hash != hashlib.md5(broken_zip_str).hexdigest():
    print "The hashes doesn't match"

# Mr. Leopold suggests that only one byte is mistaken, we are going to try to
# find this byte into the zip and fix it.
# We can suppose that the header of the file is intact, so we can ignore the
# first 30 bytes (according to the zip file format specification)
for byte in xrange(30, len(broken_zip_str)):
    for char in xrange(256):
        fixed_string = [c for c in broken_zip_str]
        fixed_string[byte] = chr(char)
        fixed_string = ''.join(fixed_string)
        if hashlib.md5(fixed_string).hexdigest() == right_hash:
            break
    else:
        continue
    break

# now, we gonna extract the image, show it and save it
fixed_zip = zipfile.ZipFile(StringIO(fixed_string))
gif_file = fixed_zip.read('mybroken.gif')

image = Image.open(StringIO(gif_file))
image.show()
image.save('mybroken.gif')

# the image says 'speed', but this doesn't lead us to any site. Then we need to
# take the monkeys' hint, "I'm missing the boat", so 'speedboat'
print "The next url is {0}{1}.html".format(pcurl, 'speedboat')
