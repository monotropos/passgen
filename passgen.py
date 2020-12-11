#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
Name: passgen.py
Date: December 2020
Purpose:
    - to generate a random password, according to a template provided as input
    - to teach Python in class
Copyright: None
"""

import sys
import re
from random import randint

data = {"l": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "c": "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ",
        "v": "aeiouAEIOU",
        "n": "0123456789",
        "s": "./,';:_-=+)(*&^%$#@!~|" }

help = """Usage:\tpassgen.py <combination of l, c, v, n, s characters> [n]
\t\tl: any character
\t\tc: consonant
\t\tv: vowel
\t\tn: number
\t\ts: symbol

\tsecond argument is number of generated strings. 1, if not defined.
\nExample: passgen.py cvcvsnn
"""

template = ""

if len( sys.argv) >1:
    # check template if it contains only l, c, v, n, s
    template = re.sub( "[^lcvns]", "", sys.argv[1])
    if len( sys.argv) > 2:
        n = int( sys.argv[2])
    else:
        n = 1
    if n<1:
        n = 1
else:
    # show help
    print( help)

if template:
    for i in range(n):
        for a in template:
            r = randint(0, len( data[a])-1)
            print( data[a][r], end="")
        print( "\n" if (i%5==4) else " ", end="")
    print("")
