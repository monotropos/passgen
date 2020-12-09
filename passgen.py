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

if len( sys.argv) >1:
    template = sys.argv[1]
else:
    template = "cnnsnn"

for a in template:
    print( a)
