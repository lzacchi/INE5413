'''
Crie um tipo estruturado de dados ou uma
classe que represente um grafo
não-dirigido e ponderadoG(V, E, w), no qual
V é o conjunto de vértices,E é o conjunto
de arestas e w:E→R é a função que mapeia
o peso de cada aresta {u, v}∈E.  As operações/métodos
contemplados para o grafo deverão ser:

    •qtdVertices(): retornr a quantidade de vértices;
    •qtdArestas(): retorna a quantidade de arestas;
    •grau(v): retorna o grau do v ́erticev;
    •rotulo(v): retorna o r ́otulo do v ́erticev;
    •vizinhos(v): retorna os vizinhos do v ́erticev;
    •haAresta(u, v): se{u, v}∈E, retorna verdadeiro; se n ̃ao existir, retorna falso;
    •peso(u, v): se{u, v}∈E, retorna o peso da aresta{u, v};
        se nao existir, retorna um valor infinito positivo1;
    •ler(arquivo)2: deve carregar um grafo a partir de um arquivo
        no formato especificado ao final deste docu-mento.'''


from math import inf
from collections import namedtuple

Graph = namedtuple("Graph", "n_vertices vertices edges n_edges")

def get_n_vertices():
    Graph.n_vertices

def get_vertices():
    Graph.vertices

def get_edges():
    Graph.edges

def degree(v):
    return( len(neighbours(v)))

# INDEX MUST TO BE > 0
def label(index):
    return [vertice[1] for vertice in Graph.vertices if vertice[0] == index][0]

def neighbours(vertice):
    result = [(u, label(u)) for ((u,v),peso) in Graph.edges if v==vertice]+[(u, label(u)) for ((u,v),peso) in Graph.edges if u==vertice]
    filtered = [t for t in result if t[0] != vertice]
    return(list(dict.fromkeys(filtered)))

def weight(u,v, directed=False):
    if directed:
        res = [edge[1] for edge in Graph.edges if edge[0] == (u,v)]
    else:
        res = [edge[1] for edge in Graph.edges if edge[0] == (u,v) or edge[0] == (v,u)]
    return res[0] if res else inf

def edge_exists(u,v):
    return( [edge for edge in Graph.edges if edge[0] == (u,v)] != [] )

def read(filename):
    file = open(filename, "r")
    txt = file.readlines()
    file.close()

    Graph.n_vertices = read_n_vertices(txt[0])
    Graph.vertices = read_vertices(txt)
    Graph.edges = read_edges(txt)
    Graph.n_edges = read_n_edges(txt)

def read_n_vertices(txt):
    return int(txt.replace("*vertices ", ""))

def read_vertices(txt):
    header_index = txt.index("*vertices " + str(Graph.n_vertices) + "\n")
    vertices_list = txt[(header_index+1):Graph.n_vertices +1]
    vertices = verticestxt_to_list(vertices_list)
    return vertices

def read_n_edges(txt):
    return len(Graph.edges)

def read_edges(txt):
    header_index = txt.index("*edges\n")
    edge_list = txt[(header_index+1):]
    edges = edgestxt_to_list(edge_list)
    return edges

def verticestxt_to_list(vertices):
    vertices_list = list()
    for vertice in vertices:
        vertice = vertice.replace('"','').replace('\n','') # cleaning string
        vertice = vertice.split(" ")

        num = int(vertice[0])
        label = vertice[1]
        vertices_list.append((num, label))
    return vertices_list

def edgestxt_to_list(edges):
    edges_list = list()
    for edge in edges:
        clean_edge = edge.replace("\n","").split(" ")

        source = int(clean_edge[0])
        dest = int(clean_edge[1])
        weight = float(clean_edge[2])
        edges_list.append(((dest, source), weight))
    return edges_list


# Tests function haha 😂😂
def ba_dum_testss():
    read("./graph-samples/custom/yt.net")

    # Tests
    print(f"Edges: {Graph.edges}")
    print(f"Num. of edges: {Graph.n_edges}\n")

    print("Weight of edges:")
    for edge in Graph.edges:
        print(f"Edge {edge[0]} weight is {weight(*edge[0])}") # unpacking edge[0] from (u,v) to u,v

    print("Check if there edges (u,v) and (v,u):")
    print("OBS: u is fixed as 1")
    for i in range(1,Graph.n_vertices+1):
        print(f"(1, {i}) ? {edge_exists(1,i)}")
        print(f"({i}, 1) ? {edge_exists(i,1)}")

    print(f"\nVertices: {Graph.vertices}")
    print(f"Num. of vertices: {Graph.n_vertices}\n")

    for vertice in Graph.vertices:
        print(f"Vertice {vertice[0]} is labeled as {label(vertice[0])}")
    print('\n')
    for vertice in Graph.vertices:
        print(f"{vertice[0]} (labeled as {vertice[1]}) degree is {degree(vertice[0])}")

    for vertice in Graph.vertices:
        print(f"{label(vertice[0])}'s neighbours are: {neighbours(vertice[0])}")

if __name__ == "__main__":
    ba_dum_testss()
