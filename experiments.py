

import networkx as nx
import matplotlib.pyplot as plt
import graphCreator as graphs
import chromaticNumber as cnum

def randomChromatic(nodes, maxedges, avgrepeat, strategy):
    clist = []
    suma = 0
    for edges in range(maxedges+1):
        for i in range(avgrepeat):
            graph = graphs.randomGraph(nodes, edges)
            c = cnum.chromaticNumber(cnum.greedy(graph,strategy))
            suma += c
        average = suma / avgrepeat
        suma = 0
        clist.append(average)
    return clist


def experiment1(nodes,maxedges):
    l = randomChromatic(nodes, maxedges, 40, nx.coloring.strategy_largest_first)
    plt.plot(l)
    plt.show()

def experiment2(nodes,maxedges, strategies):
    for s in strategies:
        l = randomChromatic(nodes, maxedges, 3, s[0])
        plt.plot(l, label=s[1])
    plt.legend(loc = 0)
    plt.show()



def prefChromatic(nodes, maxedges, avgrepeat, strategy):
    clist = []
    suma = 0
    for edges in range(maxedges):
        for i in range(avgrepeat):
            graph = graphs.prefAttach(nodes, edges+1)
            c = cnum.chromaticNumber(cnum.greedy(graph,strategy))
            suma += c
        average = suma / avgrepeat
        suma = 0
        clist.append(average)
    return clist

def experiment3(nodes, maxedges, strategies):
    for s in strategies:
        l = prefChromatic(nodes, maxedges, 3, s[0])
        plt.plot(l, label=s[1])
    plt.legend(loc = 0)
    plt.show()

# experiment3(50,30, [(nx.coloring.strategy_connected_sequential, "connected_sequential"),
#                      (nx.coloring.strategy_connected_sequential_bfs, "connected_sequential_bfs"),
#                      (nx.coloring.strategy_connected_sequential_dfs, "connected_sequential_dfs"),
#                      (nx.coloring.strategy_independent_set, "independent_set"),
#                      (nx.coloring.strategy_largest_first, "largest_first"),
#                      (nx.coloring.strategy_random_sequential, "random_sequential"),
#                      (nx.coloring.strategy_saturation_largest_first, "saturation_largest_first"),
#                      (nx.coloring.strategy_smallest_last, "smallest_last")] )

def experiment4():
    graph = graphs.randomGraph(20, 30)#graphs.prefAttach(15, 4)
    col = cnum.greedy(graph, strategy=nx.coloring.strategy_connected_sequential_dfs)
    pos = nx.spring_layout(graph, iterations=2000)
    nx.draw(graph, pos, node_color = [col[i] for i in range(20)])
    plt.show()


def clusterChromatic(nodes,maxedges,avgrepeat,strategy):
    clist = []
    suma = 0
    for edges in range(maxedges):
        for i in range(avgrepeat):
            graph = graphs.clusterGraph(nodes, edges+1, 0.9)
            c = cnum.chromaticNumber(cnum.greedy(graph,strategy))
            suma += c
        average = suma / avgrepeat
        suma = 0
        clist.append(average)
    return clist

def experiment5(nodes, maxedges, strategies):
    for s in strategies:
        l = clusterChromatic(nodes, maxedges, 3, s[0])
        plt.plot(l, label=s[1])
    plt.legend(loc = 0)
    plt.show()

experiment5(50,20, [(nx.coloring.strategy_connected_sequential, "connected_sequential"),
                     (nx.coloring.strategy_connected_sequential_bfs, "connected_sequential_bfs"),
                     (nx.coloring.strategy_connected_sequential_dfs, "connected_sequential_dfs"),
                     (nx.coloring.strategy_independent_set, "independent_set"),
                     (nx.coloring.strategy_largest_first, "largest_first"),
                     (nx.coloring.strategy_random_sequential, "random_sequential"),
                     (nx.coloring.strategy_saturation_largest_first, "saturation_largest_first"),
                     (nx.coloring.strategy_smallest_last, "smallest_last")] )

def experiment51():
    graph = graphs.clusterGraph(20, 4,0.9)#graphs.prefAttach(15, 4)
    col = cnum.greedy(graph, strategy=nx.coloring.strategy_connected_sequential_dfs)
    pos = nx.spring_layout(graph, iterations=2000)
    nx.draw(graph, pos, node_color = [col[i] for i in range(20)])
    plt.show()

#experiment51()



