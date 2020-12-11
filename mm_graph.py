import os
import sys
from collections import namedtuple

Graph = namedtuple("Graph", "n_vertices vertices X Y edges n_edges")

def read(filename):
    file = open(filename, 'r')
    txt = file.readlines()
    file.close()

    Graph.directed = False  # no directed graphs
    Graph.edges = []
    Graph.X = []
    Graph.Y = []

    for line in txt:
        if line[0] == "c":  # comments
            continue
        if line[0] == "p":  # graph info
            header = line.split()
            Graph.n_vertices = int(header[2])
            Graph.n_edges = int(header[3])
        if line[0] == "e":
            edge_line = line.split()

            src = edge_line[1]
            dest = edge_line[2]

            Graph.X.append(int(src))
            Graph.Y.append(int(dest))

            edge = (int(src), int(dest))

            Graph.edges.append(edge)

    # Remove duplicate values
    Graph.X = list(set(Graph.X))
    Graph.Y = list(set(Graph.Y))

    Graph.vertices = Graph.X + Graph.Y


def neighbours(vertice):
    neighbours = [u for (v, u) in Graph.edges if v == vertice] + [u for (u, v) in Graph.edges if v == vertice]
    filtered = [t for t in neighbours if t != vertice]  # do not count own vertice as neighbour
    return(list(set(filtered)))


def tests():
    read("./graph-samples/emparelhamento_maximo/pequeno.gr")
    print(Graph.n_vertices)
    print(Graph.X)
    print(Graph.Y)
    print(Graph.edges)
    print(Graph.n_edges)
    print(neighbours(Graph.X[0]))


if __name__ == "__main__":
    tests()
