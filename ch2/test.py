#!/usr/bin/env python3
"""tests for ch2.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './ch2.py'
decimal = ['0', '1', '2', '26', '241791', '98075434']
binary = ['0', '1', '10', '11010', '111011000001111111', '101110110001000001100101010']
hexadecimal = ['0', '1', '2', '1A', '3B07F', '5D8832A']

# --------------------------------------------------
def test_binary_to_decimal():

    for pair in zip(binary, decimal):
        rv, out = getstatusoutput(f'{prg} --bi --do {pair[0]}')
        assert rv == 0
        assert out == pair[1]

# --------------------------------------------------
def test_hexadecimal_to_decimal():
    for pair in zip(hexadecimal, decimal):
        rv, out = getstatusoutput(f'{prg} --hi --do {pair[0]}')
        assert rv == 0
        assert out == pair[1]

# --------------------------------------------------
def test_decimal_to_binary():
    for pair in zip(decimal, binary):
        rv, out = getstatusoutput(f'{prg} --di --bo {pair[0]}')
        assert rv == 0
        assert out == pair[1]

# --------------------------------------------------
def test_decimal_to_hexadecimal():
    for pair in zip(decimal, hexadecimal):
        rv, out = getstatusoutput(f'{prg} --di --ho {pair[0]}')
        assert rv == 0
        assert out == pair[1]

# --------------------------------------------------
def test_binary_to_hexadecimal():
    for pair in zip(binary, hexadecimal):
        rv, out = getstatusoutput(f'{prg} --bi --ho {pair[0]}')
        assert rv == 0
        assert out == pair[1]

# --------------------------------------------------
def test_hexadecimal_to_binary():
    for pair in zip(hexadecimal, binary):
        rv, out = getstatusoutput(f'{prg} --hi --bo {pair[0]}')
        assert rv == 0
        assert out == pair[1]
