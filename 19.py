#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 19
Title: please!
http://www.pythonchallenge.com/pc/hex/bin.html

image: web/site/map_2.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

In the html source we have an email and its attachment

"""


import array
import base64
import email
import urllib2
import re
import wave
from cStringIO import StringIO

pcurl = 'http://www.pythonchallenge.com/pc/hex/'
url = 'http://www.pythonchallenge.com/pc/hex/bin.html'

request = urllib2.Request(url)
base64string = base64.encodestring('{0}:{1}'.format('butter',
                                                    'fly')).replace('\n', '')
request.add_header("Authorization", "Basic {0}".format(base64string))
page = urllib2.urlopen(request).read()

# first we extract the email from the html source
extract_mail = re.compile('<!--\n(.*)\n-->', re.DOTALL | re.MULTILINE)
mail = re.search(extract_mail, page).group(1)

# now, get the attachment
message = email.message_from_string(mail)
attachment = message.get_payload(0)
print "The attachment is an {0} file".format(attachment.get_content_type())

# the attachment seems to be an audio wave file
filename = attachment.get_filename()
wav_file = attachment.get_payload(decode=True)
# save the file, and listen it...
with open(filename, 'wb') as original_wav:
    original_wav.write(wav_file)

# the audio file says: "sorry!"
# if we go to the url with 'sorry' we get a page with this message:
#
#   - "what are you apologizing for?"
#
# if we take a look at the hints:
#
# - a map of india
# - the name of the attachment, indian.wav
# - the body of the email, "it is so much easier for you, youngsters.
#   Maybe my computer is out of order"
#
# maybe suggests that Mr. Leopold have and old computer and maybe the byte
# order of his system could be "big-endian" (sounds like Big Indian)
# so, let's try to swap the bytes to help Mr. Leopold
original_wav = wave.open(StringIO(wav_file))

frames = array.array("H", original_wav.readframes(original_wav.getnframes()))
frames.byteswap()
fixed_wav = wave.open('indian_fixed.wav', 'wb')
fixed_wav.setparams(original_wav.getparams())
fixed_wav.writeframesraw(frames.tostring())

# if we hear the new audio, that's what it says (so elegant!):
#
#   You are and idiot!, hahaha
#
# mmm... after go to the idiot url, we have another page with the Mr. Leopold
# picture and this message:
#
#    "Now you should apologize..."
#
# and a link to the next level (idiot2.html)

print "The next url is {0}{1}.html".format(pcurl, 'idiot2')
