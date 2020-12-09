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

data = {"c": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "n": "0123456789",
        "s": "./,';:_-=+)(*&^%$#@!~|" }

if len( sys.argv) >1:
    # check template if it contains only c, n, s
    template = re.sub( "[^cns]", "", sys.argv[1])
else:
    template = "cnnsnn"

for a in template:
    r = randint(0, len( data[a])-1)
    print( data[a][r], end="")
print("")
