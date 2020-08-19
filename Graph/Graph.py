from enum import Enum
from collections import OrderedDict


class State(Enum):
    unvisited = 1       # White
    visited = 2         # Black
    visiting = 3        # Grey


class Node:
    def __init__(self, id):
        self.id = id
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()   # key = node, val = weight

    def __str__(self):
        return str(self.id)


class Graph:
    def __init__(self):
        self.nodes = OrderedDict()  # Key = node id, val = node

    def add_node(self, id):
        node = Node(id)
        self.nodes[id] = node

    def add_edge(self, source, dest, weight):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].adjacent[self.nodes[dest]] = weight


g = Graph()
g.add_edge(1, 2, 5)
g.add_edge(2, 3, 10)

print(g.nodes)
# OrderedDict([(1, <__main__.Node object at 0x000002CB5A893C70>),
#  (2, <__main__.Node object at 0x000002CB5A8CE820>),
#  (3, <__main__.Node object at 0x000002CB5A8CE850>)])
