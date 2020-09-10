#!/usr/bin/python

# Breadth First Search

import os
import sys
from graph import neighbours, read
from typing import Tuple


def bfs(n_vertices: int) -> Tuple[dict, dict]:
    visited = {}
    distance = {}
    ancestor = {}

    # Initialize structures
    for vertex in Graph.vertices:
        label = vertex[0]
        visited[label] = False
        distance[label] = float("inf")
        predecessor[label] = None

    # Add starting node
    start = Graph.vertices[0]
    start_label = start[0]
    visited[start_label] = True
    distance[start_label] = 0

    # Exploration loop
    queue = [start]
    while queue:
        current_node = queue.pop()
        cnode_label = current_node[0]

        for neightbour in neighbours(u):
            n_label = neightbour[0]
            if not visited[n_label]:
                visited[n_label] = True
                distance[n_label] = distance(cnode_label) + 1
                ancestor[n_label] = cnode_label
    return distance, ancestor

if __name__ == "__main__":
    print(f"Usage: ./{sys.argv[0] graphname}")
    os._exit(-1)

    read(sys.argv[1])
    n_vertices = Graph.n_vertices
    print(f"Total vertices: {n_vertices}")
    distance, ancestors = bfs(n_vertices)
    print(f"Distance: {distance}\nAncestors: {ancestors}")

    # Create output
    frontiers = {}
    for vertex in Graph.vertices:
        label = vertex[0]
        # check if distance key existis in output
        dist = distance[label]
        if not dist in frontiers:
            frontiers[dist] = []
        frontiers[dist].append(label)

    for k in frontiers.keys():
        print(f"{str(k)}: {frontiers[k]}")
