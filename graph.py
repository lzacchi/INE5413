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
    return(Graph.vertices[index])

def neighbours(v,labeled=False):
    result = []
    for i in range(1,Graph.n_edges+1):
        if ((v, i) in Graph.edges or (i, v) in Graph.edges):
            result.append(i)
    return(list(dict.fromkeys(result)))

def weight(u,v):
    return(Graph.edges[u,v]['weight'])

def edge_exists(u,v):
    return((u,v) in Graph.edges)

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
    vertices = verticestxt_to_dict(vertices_list)
    return vertices

def read_n_edges(txt):
    return len(Graph.edges)

def read_edges(txt):
    header_index = txt.index("*edges\n")
    edge_list = txt[(header_index+1):]
    edges = edgestxt_to_dict(edge_list)
    return edges

# input: a list like [ 'num "label"\n', 'num "label"\n', ... ]
# output: a dictionary like {num: 'label', num: 'label', ...}
def verticestxt_to_dict(vertices):
    vertices_dict = dict()
    for vertice in vertices:
        vertice = vertice.replace('"','').replace('\n','') # cleaning string
        vertice = vertice.split(" ")

        num = int(vertice[0])
        label = vertice[1]

        vertices_dict[num] = f'{label}'
    return vertices_dict

def edgestxt_to_dict(edges):
    edges_dict = dict()
    for edge in edges:
        clean_edge = edge.replace("\n","").split(" ")
        
        source = int(clean_edge[0])
        dest = int(clean_edge[1])
        weight = float(clean_edge[2])

        edges_dict[source,dest] = {'source': source, 'dest': dest, 'weight': weight}

    return edges_dict

# Tests function haha 😂😂
def ba_dum_testss():
    read("./graph-samples/custom/yt.net")

    # Tests
    print(f"Edges: {Graph.edges}")
    print(f"Num. of edges: {Graph.n_edges}\n")

    print("Weight of edges:")
    for edge in Graph.edges:
        print(f"Edge {edge} weight is {weight(edge[0],edge[1])}")


    print("Check if there edges (u,v) and (v,u):")
    print("OBS: u is fixed as 1")
    for i in range(1,Graph.n_vertices+1):
        print(f"(1, {i}) ? {edge_exists(1,i)}")
        print(f"({i}, 1) ? {edge_exists(i,1)}")

    print(f"\nVertices: {Graph.vertices}")
    print(f"Num. of vertices: {Graph.n_vertices}\n")

    for vertice in Graph.vertices:
        print(f"Vertice {vertice} is labeled as {label(vertice)}")
    print('\n')
    for vertice in Graph.vertices:
        print(f"{vertice} degree is {degree(vertice)}")

    for vertice in Graph.vertices:
        print(f"{label(vertice)}'s neighbours are: {neighbours(vertice)}")

ba_dum_testss()