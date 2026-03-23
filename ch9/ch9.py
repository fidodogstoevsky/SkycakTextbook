#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-03-23
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

    parser.add_argument('const',
                        metavar='constant',
                        type=int,
                        help='constant')

    parser.add_argument('deg',
                        metavar='degree',
                        type=int,
                        help='power')

    parser.add_argument('prec',
                        metavar='precision',
                        type=int,
                        help='precision')

    parser.add_argument('-n',
                        '--newton',
                        help='use the Newton-Raphson method',
                        action='store_true')

    args = parser.parse_args()

    if args.deg == 0:
        parser.error('degree cannot be 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    a = args.const
    n = args.deg
    p = args.prec

    if not args.newton:
        print(f'approximating {a}^(1/{n}) within precision {1/(10**p)}')
        print(f'by bisection search for root of function f(x)=x^{n}-{a}')
        print(f'yields approximation {bisection(a, n, p)}')


# --------------------------------------------------
def bisection(a, n, p):
    """calculate n-th root of constant a using bisection method
    calculated to precision decimal points"""

    # the function we're finding the root of
    def f(x):
        return x**n - a

    # find initial bounds: f(low) negative, f(up) is positive
    def start():
        low = 0
        up = 0
        while f(low) > 0:
            low -= 1
        while f(up) < 0:
            up += 1
        return (low,up)

    # improve the bounds by one step
    def step(bounds):
        low = bounds[0]
        up = bounds[1]
        mid = sum(bounds)/2
        if f(mid) > 0:
            up = mid
        elif f(mid) < 0:
            low = mid
        return (low,up)

    # iteratively improve bounds until they're within the precision margin
    def iterate(bounds):
        if abs(bounds[0]-sum(bounds)/2) < 1/(10**p):
            return bounds
        else:
            return iterate(step(bounds))

    return sum(iterate(start()))/2

# --------------------------------------------------
if __name__ == '__main__':
    main()
