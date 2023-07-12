class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def print_graph(self):
        for vertex in self.graph:
            print(vertex, "->", "->".join(str(node[0]) + ":" + str(node[1]) for node in self.graph[vertex]))

# Example usage
g = Graph()
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 1)
g.add_edge(3, 4, 3)
g.print_graph()
