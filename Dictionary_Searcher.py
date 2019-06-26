#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:39:14 2019

@author: skyking
"""

import json

with open("Dictionary.json", "r") as dict_data:
    dict_file = json.load(dict_data)
    
    
print(dict_file)