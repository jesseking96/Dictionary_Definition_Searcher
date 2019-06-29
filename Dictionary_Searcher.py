#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program will search a dictionary for a user-provided word, and return the 
definition, if it exists. If the word is not found in the dictionary, the 
program will make a suggestion for a similar word. If that new suggestion is in
the dictionary, and if the user confirms that the suggestion is the correct
word, the program will return the definition of the suggested word.
"""

import json

from spellchecker import SpellChecker

with open("Dictionary.json", "r") as dict_file:
    dict_data = json.load(dict_file)

for key in dict_data.keys():
    key = key.lower()

def get_word():
    """
    Prompts the user to input a word, checks that the word contains only
    letters, and returns the word.
    """
    while True:
        word = input("Please enter a word: ")
        if word.isalpha() == False:
            print("Invalid input. Please try again." )
            continue
        return word
    
    
def get_definition(word):
    """
    Takes in a word, and prints the definition, if it exists. If it doesn't
    exists, makes a suggestion for a similar word. If user confirms that 
    similar word is correct, returns definition of the corrected word.
    """
    global dict_data
    
    while True:   
        if word.lower() in dict_data:
            print("\n")
            print(dict_data[word.lower()])
            break

        spell = SpellChecker()
        print("Word does not exist. \n")
        word = spell.correction(word)
        if word.lower() in dict_data:
            while True:
                is_fixed = input(f"Did you mean {word} (Y/N)? ")
                if is_fixed. upper() in ["Y","N"]:
                    if is_fixed.upper() == "Y":
                        print("\n")
                        print(dict_data[word.lower()])
                        break
                    elif is_fixed.upper() == "N":
                        break
                else:
                    print("\nInvalid input. Try again. ")
                    continue
        break
        
        
def is_repeat():
    """
    Asks the user if they would like to check another word. Returns a boolean.
    """
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
        