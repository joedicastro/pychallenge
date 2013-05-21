#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 10
Title: what are you looking at?
http://www.pythonchallenge.com/pc/return/bull.html

image: web/site/bull.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

message:

    len(a[30]) = ?

in the html source the image links to a sequence:

    href="sequence.txt" />

the sequence:

    a = [1, 11, 21, 1211, 111221,

"""


# after a little research in the net, the sequence seems to be the "look and
# say" sequence (http://en.wikipedia.org/wiki/Look-and-say_sequence). Then we
# need only to generate this sequence until the 30ᵗʰ iteration.
from itertools import groupby


def look_and_say(num):
    return ''.join(str(len(list(g))) + str(d) for d, g in groupby(num))

pcurl = 'http://www.pythonchallenge.com/pc/return/'

number = '1'
for iter in xrange(30):
    number = look_and_say(number)


print "The next url is {0}{1}.html".format(pcurl, len(number))
