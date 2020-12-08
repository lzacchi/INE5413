import os
import sys
from math import inf
from collections import namedtuple
from graph import Graph

def read(filename):
    file = open(filename, 'r')
    txt = file.readlines()
    file.close()

    Graph.directed = False  # no directed graphs
    Graph.edges = []

    for line in txt:
        if line[0] == "c":  # comments
            continue
        if line[0] == "p":  # graph info
            header = line.split()
            Graph.n_vertices = int(header[2])
            Graph.n_edges = int(header[3])
            Graph.vertices = [x for x in range(1, Graph.n_vertices)]
        if line[0] == "e":
            edge_line = line.split()
            src = edge_line[1]
            dest = edge_line[2]
            edge = (int(src), int(dest))
            Graph.edges.append(edge)



# tests
def tests():
    read("./graph-samples/emparelhamento_maximo/pequeno.gr")
    print(Graph.n_vertices)
    print(Graph.vertices)
    print(Graph.edges)
    print(Graph.n_edges)


if __name__ == "__main__":
    tests()
