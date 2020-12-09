from graph import Graph, tests
# questao 1: Edmonds-Karp
def read_gr(filename):
    file = open(filename, "r")
    txt = file.readlines()
    file.close()

    Graph.directed = True
    Graph.vertices = []
    Graph.edges = []
    Graph.source = None
    Graph.sink = None

    for line in txt:
        atual = line.split(" ")
        line_type = atual[0] 

        if (line_type == "c"):
            continue

        if line_type == "p":
            Graph.n_vertices = int(atual[2])
            Graph.n_edges = int(atual[3])
            
            Graph.vertices = [(int(item), str(item)) for item in range(1, Graph.n_vertices+1)]
            Graph.capacity = [[0 for x in range(Graph.n_vertices)] for y in range(Graph.n_vertices)]

        if line_type == "a":
            source_ = int(atual[1])
            target_ = int(atual[2])
            capac_  = int(atual[3])
            arc = ((source_, target_), capac_)
            Graph.edges.append(arc)

            Graph.capacity[source_-1][target_-1] = capac_

        if line_type == "n":
            if atual[2] == 's':
                Graph.source = int(atual[1])
            
            if atual[2] == 't':
                Graph.sink = int(atual[1])

    # se nao foram definidos entao define para o primeiro e ultimo
    if Graph.source == None or Graph.sink == None:
        Graph.source = 1
        Graph.sink = Graph.n_vertices

def edmonds_karp():

    # preparando variaveis pra lidar com a matriz de capacidades
    source_ = Graph.source -1
    sink_ = Graph.sink -1

    Graph.flow = [[0]* Graph.n_vertices for f in range(Graph.n_vertices)]

    while True:
        path = Breadth_first_search()

        # caminho inexistente
        if path == None: break

        # pega os dois primeiros vertices
        u = path[0]
        v = path[1]

        # calculando fluxo atual
        flow = Graph.capacity[u][v] - Graph.flow[u][v]
        
        for i in range(len(path)-2):
            u = path[i+1]
            v = path[i+2]
            flow = min(flow, Graph.capacity[u][v] - Graph.flow[u][v])
        
        for i in range(len(path)-1):
            u = path[i]
            v = path[i+1]
            Graph.flow[u][v] += flow
            Graph.flow[v][u] -= flow
    max_flow = [Graph.flow[source_][i] for i in range(Graph.n_vertices)]
    return sum(max_flow)
    



def Breadth_first_search():
    # preparando variaveis pra lidar com a matriz de capacidades
    source_ = Graph.source -1
    sink_ = Graph.sink -1

    p = [-1] * Graph.n_vertices
    p[source_] = source_
    
    # inicializa a fila e coloca a fonte como unico elemento
    queue = [source_]

    # enquanto a fila nao for vazia
    while queue:
        u = queue.pop(0)

        for v in range(Graph.n_vertices):
            if  p[v] == -1 and Graph.capacity[u][v] - Graph.flow[u][v] > 0:
                # trocando os vertices
                p[v] = u
                queue.append(v)

                # verificando se chegou no sorvedouro
                if v == sink_:
                    path = []
                    while True:
                        path.insert(0,v)
                        
                        # interrompe se chegou na fonte
                        if v == source_:
                            break

                        v = p[v]
                    return path
    return None

if __name__ == "__main__":
    # read_gr('./graph-samples/fluxo_maximo/wiki.gr')
    # read_gr('./graph-samples/fluxo_maximo/gb128.gr')
    read_gr("./graph-samples/fluxo_maximo/teste1.gr")

    print(f"O fluxo máximo é: {edmonds_karp()}")
    print(f"source: {Graph.source}")
    print(f"sink: {Graph.sink}")
    