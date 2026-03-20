#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-03-20
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
        description="""Use roulette wheel selection to
        sample an index from a discrete probability distribution.
        To sample multiple times, use '-r' or '--repeat'.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('prob',
                        metavar='prob',
                        nargs='+',
                        type=float,
                        help='a probability')

    parser.add_argument('-r',
                        '--repeat',
                        metavar='num',
                        type=int,
                        help='number of times to sample')

    args = parser.parse_args()

    if sum(args.prob) != 1.0:
        parser.error(f'probabilities must sum to 1.0, not {sum(args.prob)}')

    if args.repeat:
        if args.repeat < 1:
            parser.error(f'must sample at least once')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dist = args.prob

    print('Sampling from distribution:')
    prettyprint(dist, 'vals', 'prob')

    if not args.repeat:
        print(f'\nResult: {random_draw(dist)}')
    else:
        totals = [0 for i in range(len(dist))]
        for run in range(args.repeat):
            result = random_draw(dist)
            totals[result] += 1
        print('\nResult:')
        prettyprint(totals, 'vals', 'cnts')




# --------------------------------------------------
def random_draw(dist):
    cumu = []
    for i in range(len(dist)):
        newval = sum(dist[:i+1])
        cumu.append(newval)

    r = random.random()
    idx = 0
    while cumu[idx] <= r:
        idx += 1
    return idx

# --------------------------------------------------
def prettyprint(vals, name1, name2):
    horiz = '+------+'
    for index in vals:
        horiz += '-----+'

    row1 = f'| {name1} |'
    for index in range(len(vals)):
        row1 += f'  {index}  |'

    row2 = f'| {name2} |'
    for item in vals:
        row2 += f' {item} |'
    print(horiz)
    print(row1)
    print(horiz)
    print(row2)
    print(horiz)

# --------------------------------------------------
if __name__ == '__main__':
    main()
