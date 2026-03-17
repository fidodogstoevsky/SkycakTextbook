#!/usr/bin/env python3
"""tests for ch1.py"""

import os
from subprocess import getstatusoutput, getoutput
import numpy as np

prg = './ch1.py'

# --------------------------------------------------
def test_symmetric():
    """check if palindromes yield True"""

    for flag in ['-s', '--symmetric']:
        for palindrome in ['racecar', 'A dog! A panic in a pagoda!', 'A man, a plan, a canal Panama!',
        'May a moody baby doom a yam?', 'Rats live on no evil star',
        'Satan, oscillate my metallic sonatas.']:
            rv, out = getstatusoutput(f'{prg} {flag} "{palindrome}"')
            assert rv == 0
            assert out == 'True'

# --------------------------------------------------
def test_symmetric_not():
    """check if non palindromes yield False"""

    for flag in ['-s', '--symmetric']:
        for non_palindrome in ['sportscar', 'dogs are animals I do believe',
        'the panama canal, oh what a canal', 'yam dam bam dram?',
        'Oh god!']:
            rv, out = getstatusoutput(f'{prg} {flag} "{non_palindrome}"')
            assert rv == 0
            assert out == 'False'

# --------------------------------------------------
def test_to_nums():
    for flag in ['-n', '--numbers']:
        rv, out = getstatusoutput(f'{prg} {flag} "a cat"')
        assert rv == 0
        assert out == '[1, 0, 3, 1, 20]'

# --------------------------------------------------
def test_to_lets():
    for flag in ['-l', '--letters']:
        rv, out = getstatusoutput(f'{prg} {flag} 1 0 3 1 20')
        assert rv == 0
        assert out == 'a cat'

# --------------------------------------------------
def test_count():
    for flag in ['-c', '--count']:
        rv, out = getstatusoutput(f'{prg} {flag} "A cat!!!"')
        assert rv == 0
        assert out == "{' ': 1, '!': 3, 'a': 2, 'c': 1, 't': 1}"


# --------------------------------------------------
def test_prime():
    for flag in ['-p', '--prime']:
        for prime in [110083, 457411, 173909, 576703, 352399,
                      261013, 7459, 814171, 198323, 604733]:
            rv, out = getstatusoutput(f'{prg} {flag} {prime}')
            assert rv == 0
            assert out == 'True'

# --------------------------------------------------
def test_prime_not():
    for flag in ['-p', '--prime']:
        for nonprime in [250954, 388902, 755486, 405288, 667614, 553858, 876620, 991748, 410976, 231010]:
            rv, out = getstatusoutput(f'{prg} {flag} {nonprime}')
            assert rv == 0
            assert out == 'False'

# --------------------------------------------------
def test_intersect():
    for flag1 in ['-1', '--arr1']:
        for flag2 in ['-2', '--arr2']:
            arrs1 = [[1,2,3],[1],[],[1,2]]
            arrs2 = [[1,2,3],[3],[4],[3,4]]
            for arr1 in arrs1:
                for arr2 in arrs2:
                    rv, out = getstatusoutput(f'{prg} {flag1} {arr1} {flag2} {arr2}')
                    assert rv == 0
                    assert out == np.intersect1d(arr1, arr2)
                

