#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Python Challange
Level 1
Title: What about making trans?
http://www.pythonchallenge.com/pc/def/map.html

image: web/site/map.jpg


###############################################################################
#                                    Hint                                     #
###############################################################################

    K->M
    O->Q
    E->G

message:

    everybody thinks twice before solving this.

    g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle
    gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle
    qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

"""


from string import maketrans

pcurl = 'http://www.pythonchallenge.com/pc/def/'

text = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr
 gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle
 qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
'''.replace('\n', '')

abc = 'abcdefghijklmnopqrstuvwxyz'
cde = 'cdefghijklmnopqrstuvwxyzab'

translation_table = maketrans(abc, cde)

print text.translate(translation_table)
print
print "The next url is {0}{1}.html".format(pcurl,
                                           'map'.translate(translation_table))
