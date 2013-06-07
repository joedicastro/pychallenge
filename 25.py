#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 25
Title: imagine how they sound
http://www.pythonchallenge.com/pc/hex/lake.html

image_file: web/site/lake1.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

in the html source code:

    <!-- can you see the waves? -->

"""

# Well, the name of the image suggests, like in previous levels, that is
# possible that could be more files like lake2.jpg, lake3.jpg, etc. And...
# Could the comment in the html source referring to wav(es) files?
# Let's find out!

import base64
import Image
import urllib2
import wave

pcurl = 'http://www.pythonchallenge.com/pc/hex/'

idx = 1
authorization = base64.b64encode('{0}:{1}'.format('butter', 'fly'))

while True:
    try:
        url = 'http://www.pythonchallenge.com/pc/hex/lake{0}.wav'.format(idx)
        request = urllib2.Request(url)
        request.add_header("Authorization", "Basic {0}".format(authorization))
        file_to_download = urllib2.urlopen(request).read()
        with open('lake{0}.wav'.format(idx), 'wb') as wave_file:
            wave_file.write(file_to_download)
        idx += 1
    except urllib2.HTTPError:
        print '{0} wav files founded and downloaded.\n'.format(idx - 1)
        break

# each audio file has 10800 frames (10800 bytes), if we take each byte as a
# color (#00→#FF) of the RGB color mode, with 3 bytes we have a pixel. So, we
# have 3600 pixels for a 60x60 image. Thinking on each little image as a piece
# from a jigsaw, we have a final 300x300 pixel image from twenty five 60x60
# pieces.
coordinates = [(x, y) for y in xrange(0, 241, 60) for x in xrange(0, 241, 60)]
jigsaw = Image.new('RGB', (300, 300))

for i in xrange(1, 26):
    wav = wave.open('lake{0}.wav'.format(i), 'rb')
    frames = wav.readframes(wav.getnframes())
    piece = Image.new('RGB', (60, 60))
    piece.fromstring(frames)
    jigsaw.paste(piece, coordinates[i - 1])

jigsaw.show()
jigsaw.save('jigsaw.jpg')

# the image says 'decent'
print "The next url is {0}{1}.html".format(pcurl, 'decent')
