import graphCreator as graphs
import chromaticNumber as cnum


graph = graphs.karateClub()

def getChromaticNumber(numberOfNodes, listOfEdges):
    coloring = cnum.getColoringHEA(numberOfNodes, listOfEdges)
    c = max(coloring)
    return c


def getCnumberWithoutOneNode(graph,node):
    edgeList = graph.edges()
    nodesList = graph.nodes()
    removedEdges = []
    for edge in range(len(edgeList)):
        if node not in edgeList[edge]:
            removedEdges.append(edgeList[edge])
    c = getChromaticNumber(len(nodesList), removedEdges)
    return c

def chromaticChanged(graph):
    chromaticList = []
    nodesList = graph.nodes()
    for node in range(len(nodesList)):
        cNumber = getCnumberWithoutOneNode(graph, node)
        chromaticList.append(cNumber)
    return chromaticList
