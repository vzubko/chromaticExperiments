

import networkx as nx

def randomGraph(nodes, edges):
    g = nx.gnm_random_graph(nodes, edges)
    return g

def prefAttach(nodes,edges):
    g = nx.barabasi_albert_graph(nodes,edges)
    return g