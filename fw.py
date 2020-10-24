# Floyd Warshall

import os
import sys
from math import inf
from pprint import pprint
from typing import List
from graph import Graph, weight, read, label


def floyd_warshall(graph: Graph) -> List[List[float]]:
    n_vertices = Graph.n_vertices

    # Initialize matrix
    dist: List[List[float]] = [[inf for i in range(n_vertices)] for j in range(n_vertices)]
    for vertex in graph.vertices:
        index = vertex[0] - 1 # 0 based indexing
        dist[index][index] = 0

    for vertex0 in graph.vertices:
        for vertex1 in graph.vertices:
            if vertex0 == vertex1: # always 0
                continue
            else:
                indexu = vertex0[0] - 1
                indexv = vertex1[0] - 1
                w = weight(vertex0[0], vertex1[0])
                dist[indexu][indexv] = w if w else inf

    for k in range(n_vertices):
        for i in range(n_vertices):
            for j in range(n_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} graphname")
        os._exit(-1)
    read(sys.argv[0])

    matrix = floyd_warshall(Graph)
    for i in range(Graph.n_vertices):
        string = str(matrix[i]).replace("[", "").replace("]", "")
        print(f"{i+1}: {string}")
