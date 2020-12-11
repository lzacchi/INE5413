import os
import sys
from math import inf

from mm_graph import Graph, neighbours, read


def bfs(graph, mate, d):
    Q = []

    for x in Graph.X:
        if mate[x] is None:
            d[x] = 0
            Q.append(x)
        else:
            d[x] = inf

    d[None] = inf

    while Q != []:
        x = Q.pop()
        if d[x] < d[None]:
            for y in neighbours(x):
                if d[mate[y]] is inf:
                    d[mate[y]] = d[x] + 1
                    Q.append(mate[y])

    return d[None] != inf


def dfs(graph, x, mate, d):
    if x:
        for y in neighbours(x):
            y2 = d[mate[y]]
            x2 = d[x] + 1
            if d[mate[y]] == (d[x] + 1):
                if dfs(graph, mate[y], mate, d):
                    mate[y] = x
                    mate[x] = y
                    return True

        d[x] = inf
        return False
    return True


def hopcroft_karp(graph: Graph):
    d = {v: inf for v in Graph.vertices}
    mate = {v: None for v in Graph.vertices}

    m = 0  # matching size

    while bfs(graph, mate, d):
        for x in Graph.X:
            if mate[x] is None:
                if dfs(graph, x, mate, d):
                    m += 1

    return m, mate


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <graph-path>")
        os._exit(-1)
    read(sys.argv[1])

    print(hopcroft_karp(Graph))
