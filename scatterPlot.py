import matplotlib.pyplot as plt
import graphCreator as graphs
import chromaticNumber as cnum
import networkx as nx
import random
import matplotlib.patches as mpatches

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
            colors.append('#5555ff')
        elif c == originalChr:
            colors.append('#ff9a00')
        else:
            colors.append('#ff0000')
    return colors

x = []
y = []
c = []
for i in range(5):
    print("graph", i)
    g = graphs.prefAttach(100, 20)
    # g = graphs.clusterGraph(random.randint(50, 200), random.randint(5, 30), random.random() * 0.5 + 0.45)
    x += getDegreeList(g)
    y += getClusteringList(g)
    c += getColorsChanged(g)


plt.scatter(x, y, c=c, s=30.0,edgecolors='face')
blue = mpatches.Patch(color='#5555ff', label='The chromatic number reduced')
orange = mpatches.Patch(color='#ff9a00', label='The chromatic number did not change')
red = mpatches.Patch(color='#ff0000', label='The chromatic number changed differently ')
plt.legend(handles=[blue,orange,red])
plt.ylabel('Clustering coefficient')
plt.xlabel('Degree')
plt.show()
