#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 17
Title: eat?
http://www.pythonchallenge.com/pc/return/romance.html

image: web/site/cookies.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

The only hint is the image

It shows somee cookies and a second image from the level 4

"""


import bz2
import cookielib
import xmlrpclib
import os
import re
import urllib
import urllib2


def get_number(text, previous=0):
    regex = re.compile('nothing(?:=|\sis\s)(\d{3,5})')
    result = regex.search(text)
    try:
        return result.groups()[0]
    except:
        return False


def cookie_info(request, cookiejar):
    for cookie in cookie_jar:
        info = cookie.value
    return info


pcurl = 'http://www.pythonchallenge.com/pc/return/'
cookie_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

# get the cookie from level 4
cookie_jar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))

request = opener.open(cookie_url)
print 'the cookie says this:\n{0}\n'.format(cookie_info(request, cookie_jar))
cookie_jar.clear()

# the cookie suggest to follow busynothing... ejem...
url_original = cookie_url + '?busynothing=12345'
url_4_links = cookie_url + '?busynothing='

# now is time to repeat the steps from level 4, but this time recollecting the
# info in the cookies
cookie_hints = []
page = opener.open(url_original).read()
print 'the page says this:\n{0}\n'.format(page)
cookie_hints.append(cookie_info(page, cookie_jar))
number = get_number(page)
url_to_follow = url_4_links + number
output = [{'url': url_original, 'number': number, 'page': page}]

for i in xrange(0, 300):
    page = opener.open(url_to_follow).read()
    cookie_hints.append(cookie_info(page, cookie_jar))
    number = get_number(page, number)
    if number:
        output += [{'url': url_to_follow, 'number': number, 'page': page}]
        url_to_follow = url_4_links + number
        cookie_jar.clear()
    else:
        print 'Error capturing data in:\n'
        print url_to_follow
        print page
        print os.linesep
        print 'Previous link:'
        last_link = output[- 1]
        print last_link['url']
        print last_link['number']
        print last_link['page']
        print os.linesep
        break

# the string stored in the cookies starts with 'BZh', the header for a BZ2
# file. Let's clean the html quotes and decompress the file
bz2_file = urllib.unquote_plus(''.join(cookie_hints))
print 'the bz2 file says this:\n{0}\n'.format(bz2.decompress(bz2_file))
with open('romance.bz2', 'wb') as out:
    out.write(bz2_file)


# Ok... another puzzle, we need to call Mozart's father... Leopold, and I
# assume that has to be in the same way as level 13
php_url = 'http://www.pythonchallenge.com/pc/phonebook.php'

server = xmlrpclib.Server(php_url)

phone = server.phone('Leopold')
print "The Leopold's phone is {0}\n".format(phone)

# Oh, my!, another false end... the page says:
#
#   no! i mean yes! but ../stuff/violin.php.
#
# And if we go to that page... with a Leopold's picture an this title:
#
#   it's me. what do you want?
#
# Well, we know that we have to bring him some flowers, so:
leopold_url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
note = 'the flowers are on their way'

# get his last cookie to change the value
for my_cookie in cookie_jar:
    my_cookie.value = note
page = opener.open(leopold_url)
print "the Leopold's page says:\n{0}\n".format(page.read())

# now, the message in the source says:
#
#   oh well, don't you dare to forget the balloons.

print "The next url is {0}{1}.html".format(pcurl, 'balloons')
