#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 22
Title: emulate
http://www.pythonchallenge.com/pc/hex/copper.html

image_file: web/site/level22.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

in the source code there is this message:

    <!-- or maybe white.gif would be more bright-->

in the joystick.html page, we get another one:

    are you in level 2, or level 22?

"""


import base64
import Image
import ImageDraw
import ImageSequence
import urllib2
from cStringIO import StringIO
from collections import defaultdict


pcurl = 'http://www.pythonchallenge.com/pc/hex/'
img_url = 'http://www.pythonchallenge.com/pc/hex/white.gif'

request = urllib2.Request(img_url)
authorization = base64.b64encode('{0}:{1}'.format('butter', 'fly'))
request.add_header("Authorization", "Basic {0}".format(authorization))
image_file = urllib2.urlopen(request).read()

with open('white.gif', 'w') as gif:
    gif.write(image_file)

image = Image.open(StringIO(image_file))

# the image is an animation of 132 frames where all pixels are black unless
# one pixel per frame. All the different pixels are inside a square of 2 pixels
# length with center in (100, 100). That characteristic, the joystick image and
# the idea of realize an OCR like in level 2, suggest that those pixels are
# like joystick movements in order to draw a letter.
# Let's write (draw) a little then...
new = Image.new('RGB', (200, 200))
letters = defaultdict(list)
moves = {100: 0, 98: -2, 102: 2}

# these coordinates are adjusted by hand, only for better aesthetics
start = {1: (20, 95),
         2: (75, 102),
         3: (95, 100),
         4: (130, 100),
         5: (180, 100)}
i = 0
for frame in ImageSequence.Iterator(image):
    for x in xrange(frame.size[0]):
        for y in xrange(frame.size[0]):
            if frame.getpixel((x, y)) != 0:
                if x == 100 and y == 100:
                    i += 1
                    letters[i].append(start.get(i))
                else:
                    letters[i].append((letters[i][-1][0] + moves.get(x),
                                      letters[i][-1][1] + moves.get(y)))


draw = ImageDraw.Draw(new)
for letter in letters:
    draw.line(letters[letter])
new.show()
new.save('emulate.gif')

# the image says bonus
print "The next url is {0}{1}.html".format(pcurl, 'bonus')
