import heapq
import os
import sys
from graph import Graph, read, label, neighbours, weight
from math import inf


def prim(graph:Graph):
    not_visited = [v[0] for v in graph.vertices]
    r = not_visited[0]
    not_visited.remove(r)

    Q = []

    A = []

    weight_sum = 0

    while not_visited:
        for neighbour in neighbours(r):
            heapq.heappush(Q, (weight(neighbour[0], r), (neighbour[0], r) ))

        while Q:
            e_weight, u = heapq.heappop(Q)

            if u[0] in not_visited:
                next_r = u[0]
                break

            if u[1] in not_visited:
                next_r = u[1]
                break

        weight_sum += e_weight
        A.append(u)
        r = next_r
        not_visited.remove(r)

    return weight_sum, A




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <graph-path>")
        os._exit(-1)
    read(sys.argv[1])

    sum_weight, edges = prim(Graph)

    print(sum_weight)
    print(edges)
