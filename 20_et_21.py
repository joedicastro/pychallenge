#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 20 & 21
Title: go away!
http://www.pythonchallenge.com/pc/hex/idiot2.html

image: web/site/unreal.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

the image shows a sign which says:

    PRIVATE PROPERTY BEYOND THIS FENCE

Message:

     but inspecting it carefully is allowed.

"""


import base64
import binascii
import bz2
import urllib2
import textwrap
import zipfile
import zlib
from cStringIO import StringIO

pcurl = 'http://www.pythonchallenge.com/pc/hex/'
img_url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'

request = urllib2.Request(img_url)
authorization = base64.b64encode('{0}:{1}'.format('butter', 'fly'))
request.add_header("Authorization", "Basic {0}".format(authorization))
page = urllib2.urlopen(request)
headers = page.headers

# after looking for various urls, files, cookies, etc... the relevant
# information was in the header when we download the 'unreal.jpg' file
for k, v in sorted(headers.items()):
    print '{0:20}→  {1}'.format(k, v)

# the chunked transfer encoding and the content-range suggest that there is
# more information available to download, let's search it
# come to certain point, no longer appear new messages, so we try by the end...
limit = int(headers['content-range'].split('/')[1])
messages = []
for i in xrange(7):
    try:
        start = int(headers['content-range'].split('/')[0].split('-')[-1]) + 1
        end = start + 1
        request.add_header('Range', 'bytes={0}-{1}'.format(start, end))
        page = urllib2.urlopen(request)
        headers = page.headers
        messages.append(page.read())
    except urllib2.HTTPError:
        start = limit - 75
        end = limit
        request.add_header('Range', 'bytes={0}-{1}'.format(start, end))
        page = urllib2.urlopen(request)
        headers = page.headers
        messages.append(page.read())

# the last message is inverted
messages[-1] = (messages[-1])[::-1]
print '\nThe messages in the hidden pages:\n\n{0}'.format('\n'.join(messages))

# the messages tell us that something is hidden at 1152983631 and the password
# is 'invader' reversed
request.add_header('Range', 'bytes={0}-{1}'.format(1152983631, end))
page = urllib2.urlopen(request)
headers = page.headers
hidden_file = page.read()

# the first two bytes of the header suggests that the file is a zip file
print "\nThe hidden file's signature: {0}\n".format(hidden_file[:2])
zip_file = hidden_file

with open('hidden.zip', 'wb') as zip:
    zip.write(hidden_file)

zip_content = zipfile.ZipFile(StringIO(zip_file))
zip_content.setpassword('redavni')
print 'The zip have 2 files: {0}\n'.format(' & '.join(zip_content.namelist()))


# Oh my! what a surprise! Hidden in the zip is a new level, the level 21!
###############################################################################
#                                  Level 21                                   #
###############################################################################


print "The 'readme.txt' says:\n\n{0}\n".format(zip_content.read('readme.txt'))

# there's another mystery file, 'package.pack'
mystery = zip_content.read('package.pack')

# if we take a look at the file's header, we can see that seems to be six
# nested files with the same signature, '789c', that corresponds with the zlib
# compression
print "The mystery file's header\n{0}\n".format(binascii.hexlify(mystery[:42]))

# decompress the mystery file is an odyssey, is nested at too much levels and
# there is two types of files inside: zlib files and bzip2 files.
# And for more suspense, there are this files reversed too, even the first has
# this header, to add more confusion:
#
# 8086 relocatable (Microsoft)
#
# that is to mislead us...
ops = {'\x78\x9c': zlib.decompress, '\x42\x5a': bz2.decompress}
logs = ''
while len(mystery) > 1:
    logs += mystery[0] if mystery[0] in ('x', 'B') else ''
    if mystery[:2] in ops.keys():
        mystery = ops[mystery[:2]](mystery)
    elif (mystery[::-1])[:2] in ops.keys():
        mystery = ops[(mystery[::-1])[:2]](mystery[::-1])
    else:
        break

# At the end, the file's content is a reversed message:
print 'The "matryoshka" like file says that: {0}\n'.format(mystery[::-1])

# looking at the 'logs' we have an ASCII banner:
print 'And the logs reveals the next level: \n'
for line in textwrap.wrap(logs.replace('B', ' '), 72):
    print line

print "\nThe next url is {0}{1}.html".format(pcurl, 'copper')
