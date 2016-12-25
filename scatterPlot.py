import matplotlib.pyplot as plt
import graphCreator as graphs
import chromaticNumber as cnum
import networkx as nx

graph = graphs.randomGraph(100,1000)

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


def getColorsChanged(graph, originalChr):
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


plt.scatter(getDegreeList(graph), getClusteringList(graph), c=getColorsChanged(graph,graphChromatic(graph)))
plt.show()