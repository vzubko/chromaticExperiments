

import networkx as nx

def greedy(g):
    greedy = nx.greedy_color(g)
    return greedy

def chromaticNumber(coloring):
    return max(coloring.values()) + 1