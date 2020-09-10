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

Graph = namedtuple("Graph", "n_vertices vertices edges")

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

def read_n_vertices(txt):
    return int(txt.replace("*vertices ", ""))


def read_vertices(txt):
    pass

def read_edges(txt):
    pass

# test
read("./graph-samples/yt.net")
print(Graph.n_vertices)
