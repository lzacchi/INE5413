import os
import sys
from graph import Graph, read, neighbours, label

def dfs(current: int, visited: dict, sorted_vertices: list):
    visited[current] = True

    for neighbour in neighbours(current):
        if not visited[neighbour]:
            dfs(neighbour, visited, sorted_vertices)

    sorted_vertices.insert(0, current)

def topsort():
    vertices = Graph.vertices
    visited: dict = {v: False for v in vertices}
    sorted_vertices = []

    # first defined node is the first one to be visited
    for current in vertices:
        if not visited[current]:
            dfs(current, visited, sorted_vertices)
    return sorted_vertices


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <graph-path>")
        os._exit(-1)
    read(sys.argv[1], directed=True)

    sorted_arr = topsort()
    sorted_arr.reverse()
    for index, v in enumerate(sorted_arr):
            print(v[1], end='')
            if index < len(sorted_arr) - 1:
                print(' -> ', end='')
    print('\n')
