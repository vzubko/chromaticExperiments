

import networkx as nx
import matplotlib.pyplot as plt
import graphCreator as graphs
import chromaticNumber as cnum

def listChromatic(nodes,maxedges,avgrepeat,strategy):
    clist = []
    suma = 0
    for edges in range(maxedges + 1):
        for i in range(avgrepeat):
            graph = graphs.randomGraph(nodes, edges)
            c = cnum.chromaticNumber(cnum.greedy(graph,strategy))
            suma += c
        average = suma / avgrepeat
        suma = 0
        clist.append(average)
    return clist


def experiment1(nodes,maxedges):
    l = listChromatic(nodes,maxedges,40,strategy = nx.coloring.strategy_largest_first)
    plt.plot(l)
    plt.show()

def experiment2(nodes,maxedges, strategies):
    for s in strategies:
        l = listChromatic(nodes,maxedges,20,strategy = s)
        plt.plot(l)
    plt.show()

experiment2(60,500, [nx.coloring.strategy_connected_sequential,
                     nx.coloring.strategy_connected_sequential_bfs,
                     nx.coloring.strategy_connected_sequential_dfs,
                     nx.coloring.strategy_independent_set,
                     nx.coloring.strategy_largest_first,
                     nx.coloring.strategy_random_sequential,
                     nx.coloring.strategy_saturation_largest_first,
                     nx.coloring.strategy_smallest_last])


