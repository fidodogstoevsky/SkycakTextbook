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
import math
from math import sin
from math import cos
from math import e

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

    parser.add_argument('init',
                        metavar='init',
                        type=float,
                        help='initial guess value')

    parser.add_argument('-a','--ascent',
                        help='gradient ascent',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    derivs = [
        [lambda x: 2*x, 'f(x)=x^2'],
        [lambda x: 2*x + 1, 'f(x)=x^2+x+1'],
        [lambda x: 4*(x**3) + 3*(x**2) - 4*x, 'f(x)=x^4+x^3-2x^2'],
        [lambda x: 3*(x**2) - 4*(x**3) - 2*x, 'f(x)=x^3-x^4-x^2'],
        [lambda x: (cos(x)/(x**2+1)) - ((2*x*sin(x))/(x**2+1)**2), 'f(x)=sin(x)/(1+x^2)'],
        [lambda x: (-3*sin(x)) + (x**2 * e**sin(x) * cos(x)) + (2*x*(e**sin(x))), 'f(x)=3cos(x)+(x^2)e^(sin(x))']
    ]
    if args.ascent:
        mode = 'ascent'
    else:
        mode = 'descent'

    print(f'using gradient {mode} to find minimum of {derivs[args.func][1]}')
    print(f'result: x={gradient_descent(derivs[args.func][0], args.alph, args.prec, args.init, args.ascent)}')

# --------------------------------------------------
def gradient_descent(fp,alpha,precision,init,asc):

    def update(x):
        """update a guess, i.e. get the n+1th guess from the nth guess
        using the formula: x_(n+1) = x_n - alpha f'(x_n)
        where alpha is the learning rate and f'(x_n) is the
        derivative of the nth guess"""
        if not asc:
            return x - alpha * fp(x)
        else:
            return x + alpha * fp(x)

    def iterate(guess,n):
        """check if a guess is within the precision range
        otherwise update it"""
        print(f'step {n}: {guess}')
        n += 1
        if abs(round(fp(guess),10)) < 1/10**precision:
            return guess
        else:
            return iterate(update(guess),n)

    # run iterate starting with the initial guess
    return iterate(init,1)



# --------------------------------------------------
if __name__ == '__main__':
    main()
