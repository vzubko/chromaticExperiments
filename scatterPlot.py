import matplotlib.pyplot as plt
import graphCreator as graphs
import chromaticNumber as cnum
import networkx as nx
import random

def getChromaticNumber(numberOfNodes, listOfEdges):
    coloring = cnum.getColoringHEA(numberOfNodes, listOfEdges)
    c = max(coloring)
    return c

def graphChromatic(graph):
    c = getChromaticNumber(len(graph.nodes()), graph.edges())
    return c

def getClusteringList(graph):
    clusterList = []
    for node in range(len(graph.nodes())):
        cluster = nx.clustering(graph,node)
        clusterList.append(cluster)
    return clusterList

def getDegreeList(graph):
    degrees = graph.degree()
    degreeList = []
    for node in range(len(graph.nodes())):
        degreeList.append(degrees[node])
    return degreeList


def getChromaticWithoutNodes(graph, listOfNodes):
    edgeList = graph.edges()
    removedEdges = []
    for edge in edgeList:
         if edge[0] not in listOfNodes and edge[1] not in listOfNodes:
            removedEdges.append(edge)
    c = getChromaticNumber(len(graph.nodes()), removedEdges)
    return c


def getColorsChanged(graph):
    originalChr = graphChromatic(graph)
    colors = []
    for node in range(len(graph.nodes())):
        c = getChromaticWithoutNodes(graph, [node])
        if c == originalChr-1:
            colors.append('green')
        elif c == originalChr:
            colors.append('yellow')
        else:
            colors.append('red')
    return colors

x = []
y = []
c = []
for i in range(5):
    print("graph", i)
    g = graphs.prefAttach(random.randint(50, 200), random.randint(5, 30))
    # g = graphs.clusterGraph(random.randint(50, 200), random.randint(5, 30), random.random() * 0.5 + 0.45)
    x += getDegreeList(g)
    y += getClusteringList(g)
    c += getColorsChanged(g)


plt.scatter(x, y, c=c)
plt.show()