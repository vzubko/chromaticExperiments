

import networkx as nx

def greedy(g,strategy):
    greedy = nx.greedy_color(g,strategy)
    return greedy

def chromaticNumber(coloring):
    return max(coloring.values()) + 1