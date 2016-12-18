import networkx as nx
import matplotlib.pyplot as plt
import graphCreator as graphs
import chromaticNumber as cnum
import time

from pyclustering.utils.graph import read_graph, draw_graph
from pyclustering.samples.definitions import GRAPH_SIMPLE_SAMPLES, GRAPH_DSJC_SAMPLES, FCPS_SAMPLES, IMAGE_REAL_SAMPLES

# graph = GRAPH_DSJC_SAMPLES.DSJC_250_5

graph = graphs.karateClub()

# degree = graph.degree()

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

print(timing(graph))






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

# print(getCnumberWithoutOneNode(graph, 2))

def chromaticChanged(graph):
    chromaticList = []
    nodesList = graph.nodes()
    for node in range(len(nodesList)):
        cNumber = getCnumberWithoutOneNode(graph, node)
        chromaticList.append(cNumber)
    return chromaticList

# print(chromaticChanged(graph))

# # start_time = time.time()
# #
# # print("Finished in %s seconds " % (time.time() - start_time))
# #
# #
# # pos = nx.spring_layout(graph, iterations=2000)
# # nx.draw(graph, pos, node_color=coloring)
# # plt.show()
