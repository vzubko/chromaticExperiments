import networkx as nx
import matplotlib.pyplot as plt
import graphCreator as graphs
import chromaticNumber as cnum
import time

from pyclustering.utils.graph import read_graph, draw_graph
from pyclustering.samples.definitions import GRAPH_SIMPLE_SAMPLES, GRAPH_DSJC_SAMPLES, FCPS_SAMPLES, IMAGE_REAL_SAMPLES

# graph = GRAPH_DSJC_SAMPLES.DSJC_250_5

graph = graphs.karateClub()

degree = graph.degree()


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
    cnumber = getChromaticNumber(len(graph.nodes()), graph.edges())
    print(cnumber)
    edgeList = graph.edges()
    removedEdges = []
    for edge in edgeList:
         if edge[0] not in listOfNodes and edge[1] not in listOfNodes:
            removedEdges.append(edge)
    c = getChromaticNumber(len(graph.nodes()), removedEdges)

    return c


