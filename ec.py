import os
import sys
from graph import Graph, read, label, neighbours
from random import randrange


def hierholzer(graph:Graph):
    e_visited = {}

    # Initially, all edges are marked unvisited
    for edge in graph.edges:
        e_visited[edge[0]] = False

    # Here we choose a vertex arbitrarily
    # In this case it's the first vertex on the Graph
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

        print(v)
        print (neighbours(v))
        for u in neighbours(v):
            print("Got here")
            edge = (v, u[0])

            print(edge)

            if e_visited[edge] == False:
                e_visited[edge] = True
                v = u[0]
                cycle.append(v)
                v_isolated = False

                print(e_visited)

                break

        if v_isolated:
            return (False, None)

        if v == t:
            break


    print("second half of algorithm")
    for x in cycle:
        for w in neighbours(x):
            print(e_visited[(x, w[0])])
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
        print(f"Usage: ./{sys.argv[0]} graphname")
        os._exit(-1)
    read(sys.argv[1])

    found, cycle = hierholzer(Graph)

    if found:
        print(1)
        print(", ".join(map(str, cycle)))
    else:
        print(0)
