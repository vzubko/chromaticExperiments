import graphCreator as graphs
import chromaticNumber as cnum
import time

graph = graphs.karateClub()

repetitions = 20

def getTime(numberOfNodes, listOfEdges):
    suma = 0
    for i in range(repetitions):
        start_time = time.time()
        cnum.getColoringHEA(numberOfNodes, listOfEdges)
        end_time = time.time() - start_time
        suma += end_time
    average = suma/repetitions
    return average

print(getTime(len(graph.nodes()), graph.edges()))


def getTimeWithoutOneNode(graph,node):
    edgeList = graph.edges()
    nodesList = graph.nodes()
    removedEdges = []
    for edge in range(len(edgeList)):
        if node not in edgeList[edge]:
            removedEdges.append(edgeList[edge])
    t = getTime(len(nodesList), removedEdges)
    return t


def timing(graph):
    timeList = []
    nodesList = graph.nodes()
    for node in range(len(nodesList)):
        t = getTimeWithoutOneNode(graph, node)
        timeList.append(t)
    return timeList
