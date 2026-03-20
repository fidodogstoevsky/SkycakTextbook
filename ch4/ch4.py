#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-03-19
Purpose: Rock the Casbah
"""

import argparse
import os
import io
import sys
import random
import re
import string
import matplotlib.pyplot as plt

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="""Monte Carlo simulation to compute probability
        of getting a certain number of heads in a certain number of
        flips of a fair coin. Use '-g' or '--graph' to generate a graph
        of all probabilities up to the chosen value.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('heads',
                    metavar='heads',
                    type=int,
                    help='number of heads for which to find the probability')

    parser.add_argument('flips',
                        metavar='flips',
                        type=int,
                        help='number of flips in each trial (MC trials are run 1000 times)')

    parser.add_argument('-g',
                        '--graph',
                        help="""calculate probability for each number of
                        heads up to the chosen value, then graph the probabilities""",
                        action='store_true')

    args = parser.parse_args()

    if args.flips < 0:
        parser.error('number of flips cannot be negative')

    if args.heads < 0:
        parser.error('number of heads cannot be negative')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_flips = args.flips
    num_heads = args.heads

    if not args.graph:
        prob = sim_probability(num_heads,num_flips)
        print(f'the probability of getting precisely {num_heads} heads in {num_flips} flips is approximately {prob}')
    else:
        probs = []
        for heads in range(0,num_flips+1):
            probs.append(sim_probability(heads,num_flips))

        print(f'probabilities: {probs}')
        print(f'sum: {sum(probs)}')

        plt.plot(probs, 'ro')
        plt.ylabel('probability')
        plt.xticks(range(0,num_flips+1))
        plt.xlabel('# of heads')
        plt.title(f'probability (y) of getting exactly (x) heads, given {num_flips} flips')
        plt.show()

# --------------------------------------------------
def sim_probability(num_heads, num_flips):
    """uses Monte Carlo simulation to compute probability
    of getting a given number of heads in a given number
    of flips of a fair coin"""
    # 1. simulate 1000 trials
    # in each trial, flip a coin num_flips times
    # and count how many heads appear
    num_trials = 1000
    total = []
    for trial in range(num_trials):
        heads = 0
        for flip in range(num_flips):
            if random.random() < 0.5:
                heads += 1
        total.append(heads)

    # 2. count the number of trails in which
    # exactly num_heads heads appeared
    # divide it by the total number of trials (1000)
    return len([count for count in total if count == num_heads])/num_trials

# --------------------------------------------------
if __name__ == '__main__':
    main()
