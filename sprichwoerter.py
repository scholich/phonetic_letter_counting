# -- coding: utf-8 --
"""Find proverbs with the phonetic letter sum of 42.

 Beware of unicode string!

"""
from __future__ import print_function
from texts import text
import re

character_lookup = {u'a': 1, u'b': 2, u'c': 2, u'd': 2, u'e': 1, u'f': 2, u'g': 2, u'h': 2, u'i': 1, u'j': 3, u'k': 2,
                    u'l': 2, u'm': 2, u'n': 2, u'o': 1, u'p': 2, u'q': 2, u'r': 2, u's': 2, u't': 2, u'u': 1, u'v': 3,
                    u'w': 2, u'x': 2, u'y': 7, u'z': 3, u'ä': 1, u'ü': 1, u'ö': 1, u'ß': 5, }


def calculate_letter_value(string):
    length = 0
    for char in string.lower():
        if char in character_lookup.keys():
            length += character_lookup[char]
    return length


def get_quotes(line):
    """Get quotes from wiki line.

    Clear annotation syntax.

    Example
    -------

        line = r'''
        * "Wo das [[Auge]] nicht sehen will, helfen weder [[Licht]] noch [[Brille|Brill]]'."
        '''
        print(get_quotes(line))

    :param line:
    :return:
    """
    quotes = []
    for match in re.findall('"([^"]*)"', line):
        explanations = re.findall('\[\[(.*?)\]\]', match)
        newstring = match
        for ex in explanations:
            newstring = newstring.replace("[[" + ex + "]]", ex.split('|')[-1])
        quotes.append(newstring)
    return quotes


quotes = []
for line in text.split("\n"):
    if len(line) == 0:
        continue
    if line[0] == "*":
        quotes.extend(get_quotes(line))

for quote in quotes:
    if calculate_letter_value(quote) == 42:
        print(quote)
