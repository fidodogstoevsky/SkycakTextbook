#!/usr/bin/env python3
"""
Author : gidonkaminer <gidon.kaminer@gmail.com>
Date   : 2026-03-12
Purpose: binary/decimal/hexadecimal converter
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
        description='Convert binary/decimal/hexadecimal to binary/decimal/hexadecimal. Choose one input --[b|d|h]i and one output --[b|d|h]o',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('string',
                        metavar='string',
                        help='input string')

    inp = parser.add_mutually_exclusive_group()

    inp.add_argument('--bi',
                    help='binary input',
                    action='store_true')

    inp.add_argument('--di',
                     help='decimal input',
                     action='store_true')

    inp.add_argument('--hi',
                     help='hexadecimal input',
                     action='store_true')

    out = parser.add_mutually_exclusive_group()

    out.add_argument('--bo',
                    help='binary output',
                    action='store_true')

    out.add_argument('--do',
                    help='decimal output',
                    action='store_true')

    out.add_argument('--ho',
                    help='hexadecimal output',
                    action='store_true')

    args = parser.parse_args()

    # check that an input format was provided
    if not any([args.bi, args.di, args.hi]):
        parser.error('must provide an input format')

    # check that an ouput format was provided
    if not any([args.bo, args.do, args.ho]):
        parser.error('must provide an output format')

    def checkinput(allowed):
        """check that the string only uses allowed characters"""
        for char in args.string:
            if char not in allowed:
                parser.error(f'must be in "{allowed}", not "{char}"')

    # check each of the input types
    if args.bi:
        checkinput('10')
    elif args.di:
        checkinput(string.digits)
    elif args.hi:
        checkinput(string.hexdigits)

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    string = args.string
    
    if args.bi and args.do:
        # binary input, decimal output
        print(binary_to_decimal(string))
    elif args.hi and args.do:
        print(hexadecimal_to_decimal(string))
    elif args.di and args.bo:
        print(decimal_to_binary(string))
    elif args.di and args.ho:
        print(decimal_to_hexadecimal(string))
    elif args.bi and args.ho:
        print(binary_to_hexadecimal(string))
    elif args.hi and args.bo:
        print(hexadecimal_to_binary(string))

# --------------------------------------------------
def binary_to_decimal(binary):
    decimal = 0
    for digit in range(len(binary)):
        decimal += int(binary[digit]) * 2**(len(binary)-1-digit)
    return str(decimal)

# --------------------------------------------------
def hexadecimal_to_decimal(hexadecimal):
    decimal = 0
    hexatrans = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}
    for digit in range(len(hexadecimal)):
        decimal += int(hexadecimal[digit].upper().translate(str.maketrans(hexatrans))) * 16**(len(hexadecimal)-1-digit)
    return str(decimal)

# --------------------------------------------------
def decimal_to_binary(decimal):
    inp = int(decimal)
    indices = []
        # count the indices at which we find the largest power of 2 that's leq to the current decimal
    most_iterations = 0
        # count how many powers of two are required at most, so we know the total length of the binary string
    while inp > 0:
        iterations = 0
        largest_power = 0
        while 2**largest_power <= inp:
            largest_power += 1
            iterations += 1
            if iterations > most_iterations:
                most_iterations = iterations
        indices.append(largest_power-1)
        inp -= 2**(largest_power-1)

    if len(indices) == 0:
        binary = '0'
    else:
        binary = ''

    for i in range(most_iterations):
        if i in indices:
            binary += '1'
        else:
            binary += '0'
    return binary[::-1]

    #return ''.join(['1' if i in indices else '0' for i in range(most_iterations)][::-1])

# --------------------------------------------------
def decimal_to_hexadecimal(decimal):
    inp = int(decimal)
    indices = {}
    most_iterations = 0
    while inp > 0:
        iterations = 0
        largest_power = 0
        while 16**largest_power <= inp:
            largest_power += 1
            iterations += 1
            if iterations > most_iterations:
                most_iterations = iterations
        largest_coef = 0
        coef = 0
        while coef * 16**(largest_power-1) <= inp:
            if coef > largest_coef:
                largest_coef = coef
            coef += 1
        if largest_power-1 not in indices.keys():
            indices[largest_power-1] = str(largest_coef)
        inp -= 16**(largest_power-1)

    if len(indices) == 0:
        hexadecimal = '0'
    else:
        hexadecimal = ''

    for i in range(most_iterations):
        if i in indices:
            if int(indices[i]) < 10:
                hexadecimal += indices[i]
            else:
                hexadecimal += 'ABCDEF'[int(indices[i])-10]
        else:
            hexadecimal += '0'

    return hexadecimal[::-1]

# --------------------------------------------------
def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    hexadecimal = decimal_to_hexadecimal(decimal)
    return hexadecimal

# --------------------------------------------------
def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    binary = decimal_to_binary(decimal)
    return binary

# --------------------------------------------------
if __name__ == '__main__':
    main()
