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


def degree():
    pass

def label():
    pass

def neighbor():
    pass

def weight():
    pass

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
    return edge_list

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

# test
read("./graph-samples/custom/yt.net")
print(Graph.n_vertices)
print(Graph.vertices)