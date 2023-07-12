from queue import Queue

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

    def bfs(self, start_vertex):
        visited = {}
        for vertex in self.adj_list:
            visited[vertex] = False
        # print(visited)
        q = Queue()
        q.put(start_vertex)
        visited[start_vertex] = True

        # while not q.empty():
        #     print(q.get())
        # print(visited)
        # i=0
        while not q.empty():
            current_vertex = q.get()
            print(current_vertex)

            for neighbor in self.adj_list[current_vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    # print(visited)
                    # print("on: ",i)
                    q.put(neighbor)
            # i+=1

g = Graph()

g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "E")
g.add_edge("D", "F")
g.add_edge("E", "F")
# print(g.adj_list)

g.bfs("A")
