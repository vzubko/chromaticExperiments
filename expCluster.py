import networkx as nx
import matplotlib.pyplot as plt
import graphCreator as graphs
import chromaticNumber as cnum

graph = graphs.clusterGraph(50,14,0.6)


print(nx.average_clustering(graph))

def getChromaticNumber(numberOfNodes, listOfEdges):
    coloring = cnum.getColoringHEA(numberOfNodes, listOfEdges)
    c = max(coloring)
    return c

def getClusteringList(graph):
    clusterList = []
    for node in range(len(graph.nodes())):
        cluster = nx.clustering(graph,node)
        clusterList.append(cluster)
    clusteringList = ['%.1f' % elem for elem in clusterList]
    return clusteringList

print(getClusteringList(graph))

def getHighestClusterNodes(graph,coefficient):
    clusterList = getClusteringList(graph)
    highestClusterNodes = []
    for node in range(len(clusterList)):
        if float(clusterList[node]) >= coefficient:
            highestClusterNodes.append(node)
    return highestClusterNodes

print(getHighestClusterNodes(graph, 0.6))


def getChromaticWithoutClusterNodes(graph, listOfNodes):
    edgeList = graph.edges()
    removedEdges = []
    for edge in edgeList:
         if edge[0] not in listOfNodes and edge[1] not in listOfNodes:
            removedEdges.append(edge)
    c = getChromaticNumber(len(graph.nodes()), removedEdges)
    return c

print(getChromaticWithoutClusterNodes(graph,getHighestClusterNodes(graph, 0.6)))


def getNodesOfSameCluster(graph, coefficient):
    clusterList = getClusteringList(graph)
    sameClusterNodes = []
    for node in range(len(clusterList)):
        if float(clusterList[node]) == coefficient:
            sameClusterNodes.append(node)
    return sameClusterNodes

print(getNodesOfSameCluster(graph,0.6))

def getChromaticRemovedOfSameCluster(graph,listOfNodes):
    chromaticList = []
    for node in range(len(listOfNodes)):
        cNumber = getChromaticWithoutClusterNodes(graph, [listOfNodes[node]])
        chromaticList.append(cNumber)
    return chromaticList

print(getChromaticRemovedOfSameCluster(graph, getNodesOfSameCluster(graph,0.7)))