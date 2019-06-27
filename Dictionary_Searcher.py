#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:39:14 2019

@author: skyking
"""

import json

from spellchecker import SpellChecker

with open("Dictionary.json", "r") as dict_file:
    dict_data = json.load(dict_file)
    

def get_word():
    while True:
        word = input("Please enter a word: ")
        if word.isalpha() == False:
            print("Invalid input. Please try again." )
            continue
        return word
    
def get_definition(word):
    
    global dict_data
    
    if word in dict_data.keys():
        print("\n")
        print(dict_data[word])
    else:
        spell = SpellChecker()
        print(f"Word does not exist. \n")
        word_guess = spell.correction(word)
        while True:
            is_fixed = input(f"Did you mean {word_guess} (Y/N)? ")
            if is_fixed. upper() in ["Y","N"]:
                if is_fixed.upper() == "Y":
                    print(dict_data[word_guess])
                    break
                else:
                    print("\nUnknown word. ")
                    break
            else:
                print("\nInvalid input. Try again. ")
        

def is_repeat():
    while True:
        repeat = input("Would you like to check another word (Y/N)? ")
        print(repeat)
        if repeat.upper() == "Y" or repeat.upper() == "N":
            return repeat.upper() == "Y"
        else:
            print("Invalid input. Please try again. ")

repeat = True

while repeat:
    
    word = get_word()
    get_definition(word)
    repeat = is_repeat()
        