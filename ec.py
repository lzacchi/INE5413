import os
import sys
from graph import Graph, read, label, neighbours
from random import randrange


def hierholzer(graph:Graph):
    edges = [edge[0] for edge in graph.edges]

    # The graphs we're working with are undirected
    # So an edge (v, u) is the same as an edge (u, v)
    # This bit check which of the "repeated" edges are
    # not present and adds them to the list
    for v in graph.vertices:
        for n in neighbours(v[0]):
            if (v[0], n[0]) not in edges:
                edges.append((v[0], n[0]))
            if (n[0], v[0]) not in edges:
                edges.append((n[0], v[0]))

    # Initially, all edges are marked unvisited
    e_visited = {edge: False for edge in edges}

    # We begin the algorithm from the first vertex
    vertex = graph.vertices[0]

    (r, cycle) = eulerian_subcycle(graph, vertex[0], e_visited)


    if not r:
        return (False, None)
    elif not all(e_visited):
        return (False, None)
    else:
        return (True, cycle)


def eulerian_subcycle(graph, v, e_visited):
    cycle = [v]
    t = v

    while True:
        v_isolated = True

        for u in neighbours(v):
            edge = (v, u[0])

            if e_visited[edge] == False and e_visited[u[0], v] == False:
                e_visited[edge] = True
                e_visited[u[0], v] = True
                v = u[0]
                cycle.append(v)
                v_isolated = False

                break

        if v_isolated:
            return (False, None)

        if v == t:
            break

    for x in cycle:
        for w in neighbours(x):
            if e_visited[(x, w[0])] == False:
                (r, aux_cycle) = eulerian_subcycle(graph, x, e_visited)
                if r == False:
                    return (False, None)
                else:
                    # append subcycles
                    cycle = cycle[:cycle.index(x)] + aux_cycle + cycle[(cycle.index(x) +1):]

    return (True, cycle)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} graphname")
        os._exit(-1)
    read(sys.argv[0])

    found, cycle = hierholzer(Graph)

    if found:
        print(1)
        print(", ".join(map(str, cycle)))
    else:
        print(0)
