

import networkx as nx
import matplotlib.pyplot as plt
import graphCreator as graphs
import chromaticNumber as cnum


def experiment1(nodes,maxedges):
    clist = []
    for edges in range(maxedges+1):
        graph = graphs.randomGraph(nodes,edges)
        c = cnum.chromaticNumber(cnum.greedy(graph))
        clist.append(c)
    plt.plot(clist)
    plt.show()

experiment1(100,1000)


