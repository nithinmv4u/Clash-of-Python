class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 not in self.adj_list:
            self.adj_list[v1] = []
        if v2 not in self.adj_list:
            self.adj_list[v2] = []
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex)
        for neighbor in self.adj_list[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

g = Graph()

g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "E")
g.add_edge("D", "F")
g.add_edge("E", "F")

g.dfs("A")
