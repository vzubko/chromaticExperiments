

import networkx as nx
import chromaticNumber as cnum
import random

def randomGraph(nodes, edges):
    g = nx.gnm_random_graph(nodes, edges)
    return g

def prefAttach(nodes,edges):
    g = nx.barabasi_albert_graph(nodes,edges)
    return g

def clusterGraph(nodes,edges,p):
    g = nx.powerlaw_cluster_graph(nodes,edges,p)
    return g

def karateClub():
    g = nx.karate_club_graph()
    return g

def randomGraphWithCNum(nodes, number, step=50):
    edges = []
    while True:
        print("Number of edges:", len(edges))
        newEdges = []
        for i in range(step):
            newEdge = (random.randrange(nodes), random.randrange(nodes))
            flippedEdge = (newEdge[1], newEdge[0])
            if newEdge not in edges and newEdge not in newEdges and flippedEdge not in edges and flippedEdge not in newEdges:
                newEdges.append(newEdge)

        c = max(cnum.getColoringHEA(nodes, edges + newEdges))
        print("c: ", c)
        while c > number:
            newEdges = newEdges[:len(newEdges)//2]
            c = max(cnum.getColoringHEA(nodes, edges + newEdges))

        edges += newEdges

        if c == number:
            break

    g = nx.Graph()
    for n in range(nodes):
        g.add_node(n)
    for (a, b) in edges:
        g.add_edge(a, b)

    return g


g = randomGraphWithCNum(40, 40, 500)
print(max(cnum.getColoringHEA(len(g.nodes()), g.edges())))