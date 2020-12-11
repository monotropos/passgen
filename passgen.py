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

if len( sys.argv) >1:
    # want help?
    if sys.argv[1] == "-h":
        # show help
        print( """Usage:
        \tpassgen.py <combination of l, c, v, n, s characters>
        \t\tl: any character
        \t\tc: consonant
        \t\tv: vowel
        \t\tn: number
        \t\ts: symbol
                """)
        template = ""
    else:
        # check template if it contains only l, c, v, n, s
        template = re.sub( "[^lcvns]", "", sys.argv[1])
else:
    template = "cvcvnnsll"

if template:
    for a in template:
        r = randint(0, len( data[a])-1)
        print( data[a][r], end="")
    print("")
