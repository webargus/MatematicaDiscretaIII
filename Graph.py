
"""
    UFRPE - BSI2019.1 - Matemática Discreta - Trabalho 2 - 2ª VA
    Dupla: Edson Kropniczki + Cristina Oliveira
    Descrição: classes simples e básicas para a implementação do algoritmo de Dijkstra,
    para cálculo da menor distância entre dois vértices de um grafo simples não-direcional
"""


class Node:

    def __init__(self, node_id):
        self.node_id = node_id              # save node id (label)
        self.edges = []                     # create blank list of edges

    # check if edge exists in this node
    def _has_edge(self, edge):
        return edge in self.edges

    # append edge to node
    def add_edge(self, other, dist):
        edge = self.Edge(self, other, dist)
        if not self._has_edge(edge):
            self.edges.append(edge)
            other.add_edge(self, dist)

    def __str__(self):
        s = "vértice %d:\n\tarestas: " % self.node_id
        if len(self.edges) > 0:
            for edge in self.edges:
                s += "\n\t%s" % edge
        else:
            s += "\n\t vértice desconectado"
        return s + "\n"

    def __eq__(self, other):
        return (self.node_id == other.node_id) and (self.edges == other.edges)

    class Edge:

        def __init__(self, n1, n2, dist):
            self.n1 = n1
            self.n2 = n2
            self.dist = dist

        def __eq__(self, other):
            return (self.n1 == other.n1) and (self.n2 == other.n2) and (self.dist == other.dist)

        def __str__(self):
            return "\tde %d a %d: %d" % (self.n1.node_id, self.n2.node_id, self.dist)


class Graph(list):

    def __init__(self):
        super(Graph, self).__init__()


"""
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.add_edge(n2, 10)
n2.add_edge(n3, 5)
n3.add_edge(n1, 7)
n3.add_edge(n4, 3)
n4.add_edge(n2, 8)
print(n1, n2, n3, n4)

"""













