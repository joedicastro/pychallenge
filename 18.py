#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 18
Title: can you tell the difference?
http://www.pythonchallenge.com/pc/return/balloons.html

image: web/site/balloons.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

In the html source we have this message:

    <!-- it is more obvious that what you might think -->

"""

# if we follow the obvious hint, and go to bright.html, that says:
#
#   ness
#
# if we go to brightness.html:
#
#   <!-- maybe consider deltas.gz -->
#
#
import base64
import difflib
import Image
import gzip
import urllib2
from cStringIO import StringIO


pcurl = 'http://www.pythonchallenge.com/pc/'
gz_url = 'http://www.pythonchallenge.com/pc/return/deltas.gz'

request = urllib2.Request(gz_url)
base64string = base64.encodestring('{0}:{1}'.format('huge',
                                                    'file')).replace('\n', '')
request.add_header("Authorization", "Basic {0}".format(base64string))
gz_file = urllib2.urlopen(request).read()
with open('deltas.gz', 'w') as out:
    out.write(gz_file)

with gzip.open('deltas.gz') as gz_file_content:
    deltas = gz_file_content.read().splitlines()

# the deltas text file are two columns of hexadecimal numbers, like an hexdump
# let's get the data from each column
column_a, column_b = [], []
for line in deltas:
    column_a.append(line[:53])
    column_b.append(line[56:])

# following the hints, let's compare the two columns
differ = difflib.Differ()
diff = differ.compare(column_a, column_b)

# now, get a different data stream for each possible situation
data = {'minuses': '', 'pluses': '', 'equals': ''}
for line in diff:
    if line[:2] == '- ':
        data['minuses'] += line[2:] + '\n'
    elif line[:2] == '+ ':
        data['pluses'] += line[2:] + '\n'
    elif line[:2] == '  ':
        data['equals'] += line[2:] + '\n'

# after analyze each data, we know that they are png files
# now, to convert each data stream in a valid file and save it
for k, v in data.items():
    binary_data = ''.join(h.decode('hex') for h in v.split())
    image = Image.open(StringIO(binary_data))
    image.show()
    image.save('{0}.png'.format(k))

# the files say:
#
# minuses.png: 'butter'
# pluses.png:  'fly'
# minuses.png: '/hex/bin.html'
#
# the first two words are the username and password for the last protected url
print "The next url is {0}{1}.html".format(pcurl, 'hex/bin')
