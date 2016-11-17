

import networkx as nx

def greedy(g):
    greedy = nx.greedy_color(g)
    return max(greedy.values()) + 1

