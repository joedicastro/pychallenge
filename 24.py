#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 24
Title: from top to bottom
http://www.pythonchallenge.com/pc/hex/ambiguity.html

image_file: web/site/maze.png


###############################################################################
#                                    Hint                                     #
###############################################################################

The only hint are the image and the title.

I suppose that we have to solve the maze

"""


import base64
import binascii
import Image
import urllib2
import zipfile
from collections import deque
from cStringIO import StringIO


def get_adjacents(pixel):
    x, y = pixel
    up, right, down, left = (x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)
    # we have to ensure that each option doesn't fall out of the maze, while we
    # can't jump over the walls
    options = []
    for option in (up, right, down, left):
        if 0 <= option[0] <= 640 and 0 <= option[1] <= 640:
            options.append(option)
    return options


def breadth_first_search(image, start, end):
    queue = deque()
    queue.append(start)
    # by changing the color of the walked steps we avoid to make another list
    # and we can see the portion of the maze that we had to explore to find the
    # exit
    image.putpixel(start, (125, 125, 125, 255))  # a gray tone
    # the collecting of the previous steps gonna get us the shortest path
    previous_step = {start: None}

    while len(queue) > 0:
        step = queue.popleft()

        if step == end:
            return previous_step

        for pixel in get_adjacents(step):
            if image.getpixel((pixel)) == (0, 0, 0, 255):  # black
                image.putpixel(pixel, (125, 125, 125, 255))
                previous_step[pixel] = step
                queue.append(pixel)
    return None


pcurl = 'http://www.pythonchallenge.com/pc/hex/'
img_url = 'http://www.pythonchallenge.com/pc/hex/maze.png'

request = urllib2.Request(img_url)
authorization = base64.b64encode('{0}:{1}'.format('butter', 'fly'))
request.add_header("Authorization", "Basic {0}".format(authorization))
img_file = urllib2.urlopen(request).read()

with open('maze.png', 'wb') as png:
    png.write(img_file)

maze = Image.open(StringIO(img_file))

# looking at the image, the white pixels seems to be the walls. At the same
# time, the rest of pixels seems to be variations of red and black. If we work
# with the image and we get only white and black pixels, it would more easy to
# deal with it. There's only one entrance (top right) and one exit (bottom
# left)
work_image = maze.copy()

for x in xrange(work_image.size[0]):
    for y in xrange(work_image.size[1]):
        if work_image.getpixel((x, y)) != (255, 255, 255, 255):
            work_image.putpixel((x, y), (0, 0, 0))

start, end = (639, 0), (1, 640)

# now we gonna explore the maze walking through it like a graph using a well
# known algorithm for the task.
previous_steps = breadth_first_search(work_image, start, end)

# now we are going to reconstruct the way out from the beginning
if previous_steps:
    previous = previous_steps.get(end)
    the_clew = [previous]
    while previous:
        previous = previous_steps.get(previous)
        if previous:
            the_clew.append(previous)

# ... and draw the path into the maze
for step in the_clew:
    work_image.putpixel((step), (255, 255, 0, 255))  # yellow

work_image.show()
work_image.save('maze_solved.png')

# while in the clew we had reconstructed the escape from the end to the start,
# the title says that we have to walk it from top to bottom, so we have to
# reverse it
yellow_brick_road = the_clew[::-1]

# let's look at that we have at the moment
print ' '.join(binascii.hexlify(chr(maze.getpixel((pixel))[0])) for pixel
               in yellow_brick_road[:12])
# seems that the odd pixels have not information at all (they are black) and in
# the even ones we can recognize this header:
#
#   50 4B 03 04 or PK\x003\x004
#
# that corresponds with a zip file
zip_file = ''.join(chr(maze.getpixel((p))[0]) for p in yellow_brick_road[1::2])
with open('maze.zip', 'wb') as zip:
    zip.write(zip_file)
zip_content = zipfile.ZipFile(StringIO(zip_file))

# let's see what is inside that file
print 'The zip have 2 files: {0}\n'.format(' & '.join(zip_content.namelist()))

# the image seems to be the key for the next level
jpg_image = Image.open(StringIO(zip_content.read('maze.jpg')))
jpg_image.show()
jpg_image.save('maze.jpg')

# the image says 'lake'
print "\nThe next url is {0}{1}.html".format(pcurl, 'lake')

# the zips file contains an image that no seems to be about this level, let's
# save the zip file for now
zip_content.extract('mybroken.zip')
