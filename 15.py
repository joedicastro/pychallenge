#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 15
Title: whom?
http://www.pythonchallenge.com/pc/return/uzi.html

image: web/site/screen15.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

in the html source:

    <!-- he ain't the youngest, he is the second -->

    <!-- todo: buy flowers for tomorrow -->

"""


import calendar


pcurl = 'http://www.pythonchallenge.com/pc/return/'

# I use the 2005 year because that seems the date in which level was published
years = []

for year in xrange(2005, 1, -1):
    if calendar.weekday(year, 1, 26) == 0:
        if str(year)[-1] == '6' and str(year)[0] == '1':
            if calendar.isleap(year):
                years.append(year)

# Following the hints, tomorrow of the second youngest year is:
print "The day is 27 January {0}\n".format(years[1])

# That day was born Wolfgang Amadeus Mozart
print "The next url is {0}{1}.html".format(pcurl, 'mozart')
