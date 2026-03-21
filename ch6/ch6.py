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
import copy

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='a file containing the arrays',
                        type=argparse.FileType('rt'))
    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    arrays = parse(args.file)
    cartprod(arrays)


# --------------------------------------------------
def parse(file):
    """parse the file that contains the arrays
    file format: each line is an array, items separated by spaces
    so arrays is an array of arrays
    """
    arrays = []
    for line in file:
        array = []
        for item in line.split():
            if item.isnumeric():
                item = int(item)
            array.append(item)
        arrays.append(array)
    return arrays

# --------------------------------------------------
def cartprod(arrays):
    points = [[]]
    for array in arrays:
        points_cp = copy.deepcopy(points)
        extensions = []
        for item in array:
            for point in points_cp:
                point_cp = copy.copy(point)
                point_cp.append(item)
                extensions.append(point_cp)
        points = extensions
    return points

# --------------------------------------------------
if __name__ == '__main__':
    main()
