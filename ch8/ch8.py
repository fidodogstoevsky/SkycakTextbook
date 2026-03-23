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
import time

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--brute',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """run either brute force or backtracking search"""

    args = get_args()

    if args.brute:
        s = time.time()
        brute_force()
        print(f'runtime: {(time.time() - s) * 1e3} milliseconds')
    else:
        s = time.time()
        back_track()
        print(f'runtime: {(time.time() - s) * 1e3} milliseconds')

# --------------------------------------------------
def brute_force():
    """brute-force search of every possible square, 9! options"""
    digits = list(range(1,10))
    square = [['_' for c in range(0,3)] for r in range(0,3)]

    for num1 in digits:
        square[0][0] = num1
        for num2 in setdiff(digits,[num1]):
            square[0][1] = num2
            for num3 in setdiff(digits,[num1,num2]):
                square[0][2] = num3
                for num4 in setdiff(digits,[num1,num2,num3]):
                    square[1][0] = num4
                    for num5 in setdiff(digits,[num1,num2,num3,num4]):
                        square[1][1] = num5
                        for num6 in setdiff(digits,[num1,num2,num3,num4,num5]):
                            square[1][2] = num6
                            for num7 in setdiff(digits,[num1,num2,num3,num4,num5,num6]):
                                square[2][0] = num7
                                for num8 in setdiff(digits,[num1,num2,num3,num4,num5,num6,num7]):
                                    square[2][1] = num8
                                    for num9 in setdiff(digits,[num1,num2,num3,num4,num5,num6,num7,num8]):
                                        square[2][2] = num9
                                        if is_valid(square):
                                            print('\nfound square:')
                                            pp(square)
    
# --------------------------------------------------
def setdiff(arr1,arr2):
    """return arr1 without the elements of arr2"""
    newarr = []
    for ele in arr1:
        if ele not in arr2:
            newarr.append(ele)
    return(newarr)

# --------------------------------------------------
def is_valid(square):
    """check if each column, row, and diagonal sums to 15"""
    # check rows
    for row in square:
        if sum(row) != 15:
            return False

    # check columns
    for col in range(0,3):
        column = []
        for row in square:
            column.append(row[col])
        if sum(column) != 15:
            return False

    # check diagonals
    diag_tl = []
    diag_tr = []
    for i in range(len(square)):
        diag_tl.append(square[i][i])
        diag_tr.append(square[i][2-i])
    for diag in [diag_tl, diag_tr]:
        if sum(diag) != 15:
            return False

    return True

# --------------------------------------------------
def is_hopeless(square):
    """check if any filled-in columns/rows/diagonals don't sum to 15"""
    # check columns
    for col in range(0,3):
        column = []
        for row in square:
            column.append(row[col])
        if ('_' not in column) and (sum(column) != 15):
            return True

    # check rows
    for row in square:
        if ('_' not in row) and sum(row) != 15:
            return True

    # check diagonals
    diag_tl = []
    diag_tr = []
    for i in range(len(square)):
        diag_tl.append(square[i][i])
        diag_tr.append(square[i][2-i])
    for diag in [diag_tl, diag_tr]:
        if ('_' not in diag) and sum(diag) != 15:
            return True

    return False


# --------------------------------------------------
def back_track():
    """backtracking search. if a square is hopeless (a row/col/diag
    is fully filled in and doesn't sum to 15) then skip that value"""
    for num1 in range(1,10):
        square = [[num1, '_', '_'],['_', '_', '_'],['_', '_', '_']]
        if is_hopeless(square): continue
        
        for num2 in range(1,10):
            if num2 == num1: continue
            square = [[num1, num2, '_'],['_', '_', '_'],['_', '_', '_']]
            if is_hopeless(square): continue
    
            for num3 in range(1,10):
                if num3 in [num1, num2]: continue
                square = [[num1, num2, num3],['_', '_', '_'],['_', '_', '_']]
                if is_hopeless(square): continue

                for num4 in range(1,10):
                    if num4 in [num1, num2, num3]: continue
                    square = [[num1, num2, num3],[num4, '_', '_'],['_', '_', '_']]
                    if is_hopeless(square): continue

                    for num5 in range(1,10):
                        if num5 in [num1, num2, num3, num4]: continue
                        square = [[num1, num2, num3],[num4, num5, '_'],['_', '_', '_']]
                        if is_hopeless(square): continue

                        for num6 in range(1,10):
                            if num6 in [num1, num2, num3, num4, num5]: continue
                            square = [[num1, num2, num3],[num4, num5, num6],['_', '_', '_']]
                            if is_hopeless(square): continue

                            for num7 in range(1,10):
                                if num7 in [num1, num2, num3, num4, num5, num6]: continue
                                square = [[num1, num2, num3],[num4, num5, num6],[num7, '_', '_']]
                                if is_hopeless(square): continue

                                for num8 in range(1,10):
                                    if num8 in [num1, num2, num3, num4, num5, num6, num7]: continue
                                    square = [[num1, num2, num3],[num4, num5, num6],[num7, num8, '_']]
                                    if is_hopeless(square): continue

                                    for num9 in range(1,10):
                                        if num9 in [num1, num2, num3, num4, num5, num6, num7, num8]: continue
                                        square = [[num1, num2, num3],[num4, num5, num6],[num7, num8, num9]]
                                        if is_hopeless(square): continue
                                        print('found square:')
                                        pp(square)

# --------------------------------------------------
def pp(square):
    for row in square:
        print(row)

# --------------------------------------------------
if __name__ == '__main__':
    main()
