#!/usr/bin/env python3
"""
Author : gidonkaminer <gidon.kaminer@gmail.com>
Date   : 2026-03-17
Purpose: Recursive sequences
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

    parser.add_argument('int',
                        metavar='number',
                        type=int,
                        help='number of terms')

    parser.add_argument('-s',
                    '--seq',
                    metavar='num',
                    help='choose sequence',)

    mode = parser.add_mutually_exclusive_group()

    mode.add_argument('-a',
                    '--array',
                    help='return an array of n terms of the sequence',
                    action='store_true')

    mode.add_argument('-r',
                    '--recursive',
                    help='return the nth term in the sequence',
                    action='store_true')

    args = parser.parse_args()

    # check that a sequence was provided
    if args.seq == None:
        parser.error('must provide a sequence')

    # check that a mode was selected (array vs recursive)
    if not any([args.array, args.recursive]):
        parser.error('must select either array or term output')

    if int(args.int) < 1:
        parser.error('input must be greater than 1')

    return args

# --------------------------------------------------
tasks = {}
task = lambda f: tasks.setdefault(f.__name__, f)

def main():
    """Make a jazz noise here"""

    args = get_args()
    num = int(args.int)
    seq = args.seq

    # funcDict = {
    #     'seq0_arr': seq0_arr,
    #     'seq0_rec': seq0_rec,
    #     'seq1_arr': seq1_arr,
    #     'seq1_rec': seq1_rec
    # }

    # if args.array:
    #     output = funcDict['seq' + str(seq) + '_arr'](num)
    # elif args.recursive:
    #     output = funcDict['seq' + str(seq) + '_rec'](num)

    # print(output)

    if args.array:
        print(tasks['seq' + str(seq) + '_arr'](num))
    elif args.recursive:
        print(tasks['seq' + str(seq) + '_rec'](num))

# --------------------------------------------------
@task
def seq0_arr(n):
    """a function that returns the first n terms of the following
    recursive sequence: starting with 3, generate each term
    by doubling the previous term and adding 1"""
    terms = [3]

    while len(terms) < n:
        prev_term = terms[-1]
        next_term = 2 * prev_term + 1
        terms.append(next_term)
    return terms

# --------------------------------------------------
@task
def seq0_rec(n):
    """a function that returns the nth term of the following
    recursive sequence: starting with 3, generate each term
    by doubling the previous term and adding 1"""
    if n == 1:
        return 3
    else:
        prev_term = seq0_rec(n-1)
        return 2 * prev_term + 1
    
    """calc_nth_term(1) returns 3, this is the base case
    if any higher input is passed, 
    """

# --------------------------------------------------
@task
def seq1_arr(n):
    terms = [5]
    while len(terms) < n:
        prev_term = terms[-1]
        next_term = 3 * prev_term - 4
        terms.append(next_term)
    return terms

# --------------------------------------------------
@task
def seq1_rec(n):
    if n == 1:
        return 5
    else:
        prev_term = seq1_rec(n-1)
        return 3 * prev_term - 4

# --------------------------------------------------
@task
def seq2_arr(n):
    terms = [25]
    while len(terms) < n:
        prev_term = terms[-1]
        if prev_term % 2 == 0:
            next_term = int(prev_term / 2)
        else:
            next_term = prev_term * 3 + 1
        terms.append(next_term)
    return terms

# --------------------------------------------------
@task
def seq2_rec(n):
    if n == 1:
        return 25
    else:
        prev_term = seq2_rec(n-1)
        if prev_term % 2 == 0:
            return int(prev_term / 2)
        else:
            return prev_term * 3 + 1

# --------------------------------------------------
@task
def seq3_arr(n):
    terms = [0,1]
    while len(terms) < n:
        prev = terms[-1]
        prev_prev = terms[-2]
        terms.append(prev + prev_prev)
    return terms[:n]
    # return only n many terms, so that when we want an array of size 1 we only get the first element
# --------------------------------------------------
@task
def seq3_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev = seq3_rec(n-1)
        prev_prev = seq3_rec(n-2)
        return prev + prev_prev

# --------------------------------------------------
@task
def seq4_arr(n):
    terms = [2,-3]
    while len(terms) < n:
        prev = terms[-1]
        prev_prev = terms[-2]
        terms.append(prev * prev_prev)
    return terms[:n]

# --------------------------------------------------
@task
def seq4_rec(n):
    if n == 0:
        return 2
    elif n == 1:
        return -3
    else:
        prev = seq4_rec(n-1)
        prev_prev = seq4_rec(n-2)
        return prev * prev_prev

# --------------------------------------------------
if __name__ == '__main__':
    main()