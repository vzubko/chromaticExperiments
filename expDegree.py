import graphCreator as graphs
import chromaticNumber as cnum


graph = graphs.karateClub()


def getChromaticNumber(numberOfNodes, listOfEdges):
    coloring = cnum.getColoringHEA(numberOfNodes, listOfEdges)
    c = max(coloring)
    return c


def getHighestDegreeNodes(graph,number):
    degrees = graph.degree()
    degreeList = []
    for node, degree in degrees.items():
        if degree >= number:
            degreeList.append(node)
    return degreeList


def getChromaticWithoutNodes(graph, listOfNodes):
    edgeList = graph.edges()
    removedEdges = []
    for edge in edgeList:
         if edge[0] not in listOfNodes and edge[1] not in listOfNodes:
            removedEdges.append(edge)
    c = getChromaticNumber(len(graph.nodes()), removedEdges)
    return c


def getNodesOfOneDegree(graph, number):
    degrees = graph.degree()
    degreeList = []
    for node, degree in degrees.items():
        if degree == number:
            degreeList.append(node)
    return degreeList

def getChromaticRemovedOfOneDegree(graph,listOfNodes):
    chromaticList = []
    for node in range(len(listOfNodes)):
        cNumber = getChromaticWithoutNodes(graph, [listOfNodes[node]])
        chromaticList.append(cNumber)
    return chromaticList

print(getChromaticRemovedOfOneDegree(graph, getNodesOfOneDegree(graph,6)))






