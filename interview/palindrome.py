#!/usr/bin/env python3

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug(logger.level)


def clean(s: str) -> str:
    '''clean removes punctuation and whitespace from string s and returns the cleaned s'''
    # Note: I assume a character that is not whitespace or punctuation is the same as asking if its alphanumeric.
    # https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string does it
    #   a little differently, the filter isn't explicit.
    return ''.join(c for c in s if c.isalnum())  ## filter out characters that aren't alphanumic


def is_palindrome(s: str) -> bool:
    '''is_palindrome returns True iff s is equal forwards and backwards without punctuation'''
    clean_s = clean(s)  # remove whitespace and punctuation
    halfway = len(clean_s) // 2  # only need to test the front half against the back half

    # Note: zip does the magic for us. It takes n iterators and packages the next item from each into a tuple,
    # making the comparison easy. all completes the magic.
    return all(front == back for (front, back) in zip(clean_s[:halfway + 1], clean_s[-1: halfway - 1:-1]))

# See ../tests/test_palindrome.py to test the implementation.

# def main(argv):
#     logger.debug(is_palindrome(" %%%%%\t 121!! "))
#     logger.debug(is_palindrome("1234"))
#
# if '__main__' == __name__:
#     main(sys.argv)
