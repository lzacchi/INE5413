import os
import sys
from math import inf
from collections import namedtuple

def read(filename):
    file = open(filename, 'r')
    txt = file.readlines()
    file.close()

    for line in txt:
        if line[0] == "c":  # comments
            continue
        if line[0] == "p":  # graph info
            pass

def read_n_vertices():
    pass

def read_n_edges():
    pass
