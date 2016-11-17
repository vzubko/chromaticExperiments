

import networkx as nx
import matplotlib.pyplot as plt
import graphCreator as graphs
import chromaticNumber as cnum


def experiment1(nodes,maxedges):
    clist = []
    suma = 0
    for edges in range(maxedges+1):
        for i in range(10):
            graph = graphs.randomGraph(nodes,edges)
            c = cnum.chromaticNumber(cnum.greedy(graph))
            suma += c
        average = suma/10
        suma = 0
        clist.append(average)
    plt.plot(clist)
    plt.show()

experiment1(100,1000)


