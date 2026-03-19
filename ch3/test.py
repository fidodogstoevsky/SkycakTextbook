#!/usr/bin/env python3
"""tests for ch3.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './ch3.py'
seq0 = [3,7,15,31,63,127,255,511]
seq1 = [5,11,29,83,245,731,2189,6563]
seq2 = [25,76,38,19,58,29,88,44]
seq3 = [0, 1, 1, 2, 3, 5, 8, 13]
seq4 = [2,-3,-6,18,-108,-1944,209952,-408146688]

# --------------------------------------------------
def test_seq0_arr():
    """iterate through each length of the sequence,
    verify the output is the same regardless of desired length"""
    for length in range(1,len(seq0)):
        rv, out = getstatusoutput(f'{prg} {length} --array --seq 0')
        assert rv == 0
        assert out == str(seq0[:length])

# --------------------------------------------------
def test_seq0_rec():
    for index in range(1,len(seq0)):
        rv, out = getstatusoutput(f'{prg} {index} --recursive --seq 0')
        assert rv == 0
        assert out == str(seq0[index-1])

# --------------------------------------------------
def test_seq1_arr():
    for length in range(1,len(seq1)):
        rv, out = getstatusoutput(f'{prg} {length} --array --seq 1')
        assert rv == 0
        assert out == str(seq1[:length])

# --------------------------------------------------
def test_seq1_rec():
    for index in range(1,len(seq1)):
        rv, out = getstatusoutput(f'{prg} {index} --recursive --seq 1')
        assert rv == 0
        assert out == str(seq1[index-1])

# --------------------------------------------------
def test_seq2_arr():
    for length in range(1,len(seq2)):
        rv, out = getstatusoutput(f'{prg} {length} --array --seq 2')
        assert rv == 0
        assert out == str(seq2[:length])

# --------------------------------------------------
def test_seq2_rec():
    for index in range(1,len(seq2)):
        rv, out = getstatusoutput(f'{prg} {index} --recursive --seq 2')
        assert rv == 0
        assert out == str(seq2[index-1])

# --------------------------------------------------
def test_seq3_arr():
    for length in range(1,len(seq3)):
        rv, out = getstatusoutput(f'{prg} {length} --array --seq 3')
        assert rv == 0
        assert out == str(seq3[:length])

# --------------------------------------------------
def test_seq3_rec():
    for index in range(1,len(seq3)):
        rv, out = getstatusoutput(f'{prg} {index} --recursive --seq 3')
        assert rv == 0
        assert out == str(seq3[index])

# --------------------------------------------------
def test_seq4_arr():
    for length in range(1,len(seq4)):
        rv, out = getstatusoutput(f'{prg} {length} --array --seq 4')
        assert rv == 0
        assert out == str(seq4[:length])

# --------------------------------------------------
def test_seq4_rec():
    for index in range(1,len(seq4)):
        rv, out = getstatusoutput(f'{prg} {index} --recursive --seq 4')
        assert rv == 0
        assert out == str(seq4[index])

# class Seq:
#     def arr(self):
#         for length in range(1,len(seq0)):
#             rv, out = getstatusoutput(f'{prg} {length} --array --seq 0')
#             assert rv == 0
#             assert out == str(seq0[:length])

#     def rec(self):
#         for index in range(1,len(seq0)):
#             rv, out = getstatusoutput(f'{prg} {index} --recursive --seq 0')
#             assert rv == 0
#             assert out == str(seq0[index-1])


# class TestSeq0(Seq):
#     # --------------------------------------------------
#     def test_seq0_arr(self):
#         """iterate through each length of the sequence,
#         verify the output is the same regardless of desired length"""
#         for length in range(1,len(seq0)):
#             rv, out = getstatusoutput(f'{prg} {length} --array --seq 0')
#             assert rv == 0
#             assert out == str(seq0[:length])

#     # --------------------------------------------------
#     def test_seq0_rec(self):
#         for index in range(1,len(seq0)):
#             rv, out = getstatusoutput(f'{prg} {index} --recursive --seq 0')
#             assert rv == 0
#             assert out == str(seq0[index-1])




