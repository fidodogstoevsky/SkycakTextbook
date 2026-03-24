#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-03-24
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

    parser.add_argument('func',
                        metavar='func',
                        type=int,
                        help='function to minimize')

    parser.add_argument('alph',
                        metavar='alpha',
                        type=float,
                        help='learning rate')

    parser.add_argument('prec',
                        metavar='precision',
                        type=int,
                        help='stop descent when lower than 1/10**p')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    derivs = [
        [lambda x: 2*x, 'f(x)=x^2'],
        [lambda x: 2*x + 1, 'f(x)=x^2 + x + 1'],
        [lambda x: 3*(x**2) - 4*(x**3) - 2*x, 'f(x)=x^3 - x^4 - x^2']
    ]

    print(f'using gradient descent, minimum of {derivs[args.func][1]} is x={gradient_descent(derivs[args.func][0], args.alph, args.prec)}')

# --------------------------------------------------
def gradient_descent(fp,alpha,precision):

    def update(x):
        return x - alpha * fp(x)

    def iterate(guess):
        if round(fp(guess),10) < 1/10**precision:
            return guess
        else:
            return iterate(update(guess))

    return iterate(1)


# --------------------------------------------------
if __name__ == '__main__':
    main()
