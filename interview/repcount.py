#!/usr/bin/env python3

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug(logger.level)

import sys
import re

def render_count(count:int)->str:
    '''
    Used to render the repetition count in the generated string.
    If the count is 1, return the empty string otherwise return the count.
    :param count: number of repetitions, count >= 1 always
    :return: '' or the count
    '''
    if count == 1: return ''   # the "default"
    return str(count)  # the actual count

def crunch(s:str)->str:
    '''
    Return a character and it's repetition count if the count is greater than 1. For example, 'AAABBBC' => 'A3B3C'
    :param s: input string
    :return: "repetition string"
    '''

    result = list()
    position = 0
    last = len(s) - 1

    # For each new character grouping ...
    while position <= last:
        # Find the character at the beginning of the group
        c = s[position]
        # Create a dynamic regular expression pattern that matches just that sequence of characters 1 or more times.
        # You now you'll always match. Note that the expression contains parens, go you can get a "match group".
        letters = re.match(f'({c})+', s[position:])
        # Get the number of letters matched
        count = len(letters.group(0))
        # If it's two or more, create a rep count
        result.append(f"{c}{render_count(count)}")
        # move right by the number of matches
        position += count

    # Join the intermediate results and return that string.
    return ''.join(result)





def main(argv):
    assert(crunch('') == '')
    assert(crunch('AAABBBC') == 'A3B3C')
    assert(crunch('ABAB') == 'ABAB')
    assert(crunch('AAB') == 'A2B')



if '__main__' == __name__:
    main(sys.argv)
