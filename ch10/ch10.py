#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-03-24
Purpose: Gradient Descent
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
        description="""Find min/max of function by gradient descent/ascent.
        Functions are labeled 0 to 4. By default, runs gradient descent
        with initial guess init. For ascent, '-a'/'--ascent'.
        To try a range of initial guesses, give upper bound with
        '-u'/'--upper' (then init is lower bound).""",
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
                        metavar='int',
                        type=int,
                        help='initial guess value')

    parser.add_argument('-a','--ascent',
                        help='gradient ascent',
                        action='store_true')

    parser.add_argument('-u', '--upper',
                        help='upper bounds for guesses',
                        metavar='int',
                        type=int)

    args = parser.parse_args()

    if args.upper:
        if args.upper < args.init:
            parser.error('upper bound must be at least equal to lower bound')

    return args


# --------------------------------------------------
def main():
    """calculate minimum of function by gradient descent/ascent"""

    derivs = [
        [lambda x: 2*x, 'f(x)=x^2', lambda x: x**2],
        [lambda x: 2*x + 1, 'f(x)=x^2+x+1', lambda x: x**2 + x + 1],
        [lambda x: 4*(x**3) + 3*(x**2) - 4*x, 'f(x)=x^4+x^3-2x^2', lambda x: x**4 + x**3 - 2*x**2],
        [lambda x: 3*(x**2) - 4*(x**3) - 2*x, 'f(x)=x^3-x^4-x^2', lambda x: x**3 - x**4 - x**2],
        [lambda x: (cos(x)/(x**2+1)) - ((2*x*sin(x))/(x**2+1)**2), 'f(x)=sin(x)/(1+x^2)', lambda x: sin(x)/(1+x**2)],
        [lambda x: (-3*sin(x)) + (x**2 * e**sin(x) * cos(x)) + (2*x*(e**sin(x))), 'f(x)=3cos(x)+(x^2)e^(sin(x))', lambda x: 3*cos(x) + (x**2)*(e**sin(x))]
    ]

    args = get_args()
    func_name = derivs[args.func][1]
    func = derivs[args.func][2]
    deriv = derivs[args.func][0]
    alph = args.alph
    prec = args.prec
    asc = args.ascent
    init = args.init

    if asc:
        mode = ['ascent','maximum']
    else:
        mode = ['descent','minimum']

    print(f'using gradient {mode[0]} to approximate {mode[1]} of {func_name}')
    if not args.upper:
        x = gradient_descent(deriv, alph, prec, init, asc)
        print(f'result: x={x}, f(x)={func(x)}')
    else:
        upper = args.upper
        print(f'trying initial guesses from {init} to {upper}')
        # for start in range(init,upper):
        #     print(f'for inital guess {guess}: x={gradient_descent(deriv, alph, prec, guess, asc)}')
        xs = []
        for start in range(init,upper):
            try:
                x = gradient_descent(deriv, alph, prec, start, asc)
                xs.append(x)
            except OverflowError:
                pass
            except RecursionError:
                pass
        f_xs = list(map(func,xs))

        min_ind = 0
        for i in range(len(f_xs)):
            if f_xs[i] < f_xs[min_ind]:
                min_ind = i
            
        print(f'result: x={xs[min_ind]}, f(x)={f_xs[min_ind]}')


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

    def iterate(guess, n):
        """check if a guess is within the precision range
        otherwise update it"""
        #print(f"step {n}: x={guess}, f'(x)={fp(guess)}")
        if abs(round(fp(guess),10)) < 1/10**precision:
            return guess
        else:
            return iterate(update(guess), (n+1))

    # run iterate starting with the initial guess
    # the second argument (1) is just for debugging,
    # for counting the number of steps
    return iterate(init, 1)

# --------------------------------------------------
if __name__ == '__main__':
    main()
