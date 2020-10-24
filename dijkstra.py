# Dijkstra algorithm
import os
import sys
from math import inf
from pprint import pprint
from typing import List, Tuple
from graph import Graph, weight, read, label, neighbours

def dijkstra(graph: Graph, start: tuple) -> Tuple[dict,dict]:
    distance = {}
    ancestor = {}
    visited = {}

    # Initialize structures
    for vertex in Graph.vertices:
        v_id = vertex[0]
        distance[v_id] = float("inf")
        ancestor[v_id] = None
        visited[v_id] = False

    start_v_id = start[0]
    distance[start_v_id] = 0

    while False in visited.values():
        non_visited_distance = {k: distance[k] for k,v in visited.items() if v == False}
        u = min(non_visited_distance, key=non_visited_distance.get)
        visited[u] = True
        for vertex in neighbours(u):
            v = vertex[0]
            if visited[v] == False:
                if distance[v] > distance[u] + weight(u,v):
                    distance[v] = distance[u] + weight(u,v)
                    ancestor[v] = u
    return distance, ancestor

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <graph-path>")
        os._exit(-1)
    read(sys.argv[0])

    n_vertices = Graph.n_vertices
    print(f"Total vertices: {n_vertices}")
    # distance, ancestors =dijkstra(Graph,(1,'A'))
    distance, ancestors =dijkstra(Graph,(1))
    # distance, ancestors =dijkstra(Graph,('A'))
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

    for k in sorted(frontiers.keys()):
        print(f"{str(k)}: {frontiers[k]}")
