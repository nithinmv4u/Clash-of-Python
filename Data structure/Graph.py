class Graph:
    def __init__(self):
        self.adj_list = {}
 
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
 
    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adj_list:
            self.add_vertex(vertex2)
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)
 
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].remove(vertex2)
            self.adj_list[vertex2].remove(vertex1)
 
    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            del self.adj_list[vertex]
            for key in self.adj_list:
                if vertex in self.adj_list[key]:
                    self.adj_list[key].remove(vertex)
 
    def get_vertices(self):
        return list(self.adj_list.keys())
 
    def get_edges(self):
        edges = []
        for vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                edges.append((vertex, neighbor))
        return edges
    
# Create a graph
g = Graph()

# Add some vertices
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

# Add some edges
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('D', 'A')
g.add_edge('D', 'E')

# Print out the vertices
print('Adjacent List:', g.adj_list)

# Print out the vertices
print('Vertices:', g.get_vertices())

# Print out the edges
print('Edges:', g.get_edges())

# Remove a vertex and an edge
g.remove_vertex('C')
g.remove_edge('A', 'B')

# Print out the vertices and edges again
print('Vertices:', g.get_vertices())
print('Edges:', g.get_edges())
