#!/usr/bin/env python3
"""
Author : gidonkaminer <gidon.kaminer@gmail.com>
Date   : 2026-03-04
Purpose: string manupulation
"""

import argparse
import os
import io
import sys
import random
import re
import string
from subprocess import getstatusoutput, getoutput
import math

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='string manipulation',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--symmetric',
                        help='check if input is symmetric',
                        type=str)

    parser.add_argument('-n',
                        '--numbers',
                        help='convert input letters to numbers',
                        type=str)

    parser.add_argument('-l',
                        '--letters',
                        help='convert input numbers to letters',
                        nargs='+',
                        type=int)

    parser.add_argument('-c',
                        '--count',
                        help='count unique characters',
                        type=str)

    parser.add_argument('-p',
                        '--prime',
                        help='check if prime',
                        type=int)

    parser.add_argument('-i',
                        '--intersect',
                        help='check if intersecting',
                        nargs=2,
                        type=str)

    parser.add_argument('-1',
                        '--arr1',
                        help='the first array',
                        nargs='+',
                        type=int)

    parser.add_argument('-2',
                        '--arr2',
                        help='the second array',
                        nargs='+',
                        type=int)

    args = parser.parse_args()

    if args.prime:
        if not 1 < args.prime:
            parser.error(f'--prime "{args.prime}" must be greater than 1')

            


    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if args.symmetric:
        print(symmetric(args.symmetric))
    elif args.numbers:
        print(to_nums(args.numbers))
    elif args.letters:
        print(to_lets(args.letters))
    elif args.count:
        print(count(args.count))
    elif args.prime:
        print(prime(args.prime))

# --------------------------------------------------
def symmetric(text):
    letters = [char.lower() for char in text if char.isalpha()]
    return letters == letters[::-1]
        # python list slices [a:b:c]
        # a is the start of the slice (includes a)
        # b is the end of the slice (doesn't include b)
        # c is the interval
        # [::-1] means a slice from start to end of string,
        # at interval each index, but in reverse index order (-1)

# --------------------------------------------------
def to_nums(text):
    """ converts letters (and space) to ints, tosses everything else"""
    alphabet = ' ' + string.ascii_lowercase
    return [alphabet.index(char) for char in text if char in alphabet]
    # the index() method returns the position at the
    # first occurrence of the specified value
    # so alphabet.index(char) is the first occurrence of
    # char in the alphabet

# --------------------------------------------------
def to_lets(numlist):
    """ converts list of ints to letters (and space)
    argparse ensures that only ints are given as input"""
    alphabet = ' ' + string.ascii_lowercase
    return ''.join([alphabet[char] for char in numlist])

# --------------------------------------------------
def count(text):
    characters = list(text.lower())
    chardict = {char: characters.count(char) for char in characters}
    sorted_keys = sorted(chardict)
    return {key: chardict[key] for key in sorted_keys}
    # without list.count() method
    # print({char: sum([1 for checkchar in characters if checkchar == char]) for char in characters})

# --------------------------------------------------
def prime(num):
    is_prime = True
    for i in range(2, math.floor(num/2)):
        if (num/i).is_integer():
            is_prime = False
            break
    return is_prime

# --------------------------------------------------
if __name__ == '__main__':
    main()