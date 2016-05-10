import random

import networkx as nx


class BaseGraph:

    graph = None

    def __init__(self,n,p):
        self.graph = nx.erdos_renyi_graph(n,p)
        return

    def choose_randome_edge(self):
        return random.choice(self.graph.edges())

    def has_edge(self, a, b):
        return self.graph.has_edge(a, b)

    def get_edges_num(self, node_list):
        sub = self.graph.subgraph(node_list)
        return sub.edges().__len__()

    def get_number_of_edges(self):
        return len(self.graph.edges())


