import networkx as nx
import graphCreator as graphs
import chromaticNumber as cnum

graph = graphs.clusterGraph(50,14,0.6)


def getChromaticNumber(numberOfNodes, listOfEdges):
    coloring = cnum.getColoringHEA(numberOfNodes, listOfEdges)
    c = max(coloring)
    return c

def getClusteringList(graph):
    clusterList = []
    for node in range(len(graph.nodes())):
        cluster = nx.clustering(graph,node)
        clusterList.append(cluster)
    clusteringList = [int(elem * 10) for elem in clusterList]
    return clusteringList


def getHighestClusterNodes(graph,coefficient):
    clusterList = getClusteringList(graph)
    highestClusterNodes = []
    for node in range(len(clusterList)):
        if float(clusterList[node]) >= coefficient:
            highestClusterNodes.append(node)
    return highestClusterNodes


def getChromaticWithoutClusterNodes(graph, listOfNodes):
    edgeList = graph.edges()
    removedEdges = []
    for edge in edgeList:
         if edge[0] not in listOfNodes and edge[1] not in listOfNodes:
            removedEdges.append(edge)
    c = getChromaticNumber(len(graph.nodes()), removedEdges)
    return c


def getNodesOfSameCluster(graph, coefficient):
    clusterList = getClusteringList(graph)
    sameClusterNodes = []
    for node in range(len(clusterList)):
        if clusterList[node] == int(coefficient*10):
            sameClusterNodes.append(node)
    return sameClusterNodes


def getChromaticRemovedOfSameCluster(graph,listOfNodes):
    chromaticList = []
    for node in range(len(listOfNodes)):
        cNumber = getChromaticWithoutClusterNodes(graph, [listOfNodes[node]])
        chromaticList.append(cNumber)
    return chromaticList

print(getChromaticRemovedOfSameCluster(graph, getNodesOfSameCluster(graph,0.7)))