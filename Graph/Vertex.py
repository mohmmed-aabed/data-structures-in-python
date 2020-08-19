class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def get_id(self):
        return self.id

    def add_neighbour(self, neighbour, weight=0):
        self.connected_to[neighbour] = weight

    def get_weight(self, neighbour):
        return self.connected_to[neighbour]

    def get_connections(self):
        return self.connected_to.keys()

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex

    def get_vertex(self, key):
        if key in self.vert_list:
            return self.vert_list[key]
        else:
            return None

    def get_vertices(self):
        return self.vert_list.keys()

    def add_edge(self, f, t, cost=0):
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)
        self.vert_list[f].add_neighbour(self.vert_list[t], cost)

    def __iter__(self):
        return iter(self.vert_list.values())


graph = Graph()
for num in range(1, 6):
    graph.add_vertex(num)

print(graph.vert_list)
# {1: <__main__.Vertex object at 0x000002B4A69A3C40>,
# 2: <__main__.Vertex object at 0x000002B4A69B26D0>,
# 3: <__main__.Vertex object at 0x000002B4A69B27F0>,
# 4: <__main__.Vertex object at 0x000002B4A69B2850>,
# 5: <__main__.Vertex object at 0x000002B4A69B28B0>}

graph.add_edge(1, 2, 5)
graph.add_edge(2, 3, 10)
graph.add_edge(3, 4, 15)
graph.add_edge(4, 5, 20)
graph.add_edge(5, 1, 25)

for vertex in graph:
    print(vertex)
# 1 connected to: [2]
# 2 connected to: [3]
# 3 connected to: [4]
# 4 connected to: [5]
# 5 connected to: [1]
