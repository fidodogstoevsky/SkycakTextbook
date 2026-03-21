#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-03-21
Purpose: Rock the Casbah
"""

import argparse
import os
import io
import sys
import random
import re
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('message',
                        metavar='str',
                        type=str,
                        help='the string to be encoded')

    parser.add_argument('a',
                        metavar='int',
                        type=int,
                        help='coefficient "a" for encoding function')

    parser.add_argument('b',
                        metavar='int',
                        type=int,
                        help='coefficient "b" for encoding function')

    parser.add_argument('-u',
                        '--upperbound',
                        metavar='int',
                        type=int,
                        nargs=2,
                        help='upper bounds on "a" and "b"')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    message = args.message

    if not args.upperbound:
        a = args.a
        b = args.b
        print(f'alphabetic message: "{message}"')
        print(f'numerical message:  {to_num(message)}')
        print(f'encoding function:  f(x)={a}x+{b}')
        print(f'encoded numerals:   {encode_string(message, a, b)}')
        print(f'decoding function:  f(x)=(x-{b})/{a}')
        print(f'decoded message:    "{''.join(to_alp(decode_numbers(encode_string(message, a, b), a, b)))}"')
    else:
        a = range(args.a, args.upperbound[0])
        b = range(args.b, args.upperbound[1])

# --------------------------------------------------
def encode_string(message, a, b):
    """encodes message by changing each character
    according to linear encoding function f(x)=ax+b"""
    return list(map(lambda x: a*x + b, to_num(message)))
    
# --------------------------------------------------
def decode_numbers(numbers, a, b):
    """decodes numbers array, assuming linear encoding function f(x)=ax+b
    returns a message if the numbers represent one, and False otherwise"""
    decoded = list(map(lambda x: (x-b)/a, numbers))
    if all(list(map(lambda x: x.is_integer() and 0 <= x < 27, decoded))):
        return list(map(lambda x: int(x), decoded))
    else:
        return False

# --------------------------------------------------
def to_num(lets):
    return [(' ' + string.ascii_lowercase).index(c) for c in lets.lower()]

# --------------------------------------------------
def to_alp(nums):
    return [(' ' + string.ascii_lowercase)[n] for n in nums]

# --------------------------------------------------
if __name__ == '__main__':
    main()
