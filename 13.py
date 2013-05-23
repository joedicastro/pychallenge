#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Python Challenge
Level 13
Title: call him
http://www.pythonchallenge.com/pc/return/disproportional.html

image: web/site/disprop.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

message:

    phone that evil

the image is linked to php file called phonebook.php

This page returns a XML file with that message:

<methodResponse>
    <fault>
        <value>
            <struct>
                <member>
                    <name>faultCode</name>
                    <value>
                        <int>
                            105
                        </int>
                    </value>
                </member>
                <member>
                    <name>faultString</name>
                    <value>
                        <string>
                            XML error: Invalid document end at line 1, column 1
                        </string>
                    </value>
                </member>
            </struct>
        </value>
    </fault>
</methodResponse>

Thath is a standard error for a xml-rpc server

"""


import xmlrpclib

pcurl = 'http://www.pythonchallenge.com/pc/return/'
php_url = 'http://www.pythonchallenge.com/pc/phonebook.php'

server = xmlrpclib.Server(php_url)

# get the available methods in the server
methods = '\n'.join(server.system.listMethods())
print 'The methods available in the server are:\n\n{0}\n'.format(methods)

# there is a 'phone' method, let's see what it does
print 'The "phone" method: {0}\n'.format(server.system.methodHelp('phone'))

# let's get his phone, from that evil. I suppose that evil is the one from
# level 12, the infamous 'Bert'
phone = server.phone('Bert')
print "The Bert's phone is {0}\n".format(phone)

print "The next url is {0}{1}.html".format(pcurl, phone.split('-')[1])
