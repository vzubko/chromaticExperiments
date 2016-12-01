

import networkx as nx
import subprocess

GRAPH_FILE_PATH = "/tmp/graph.txt"
BASE_PATH = "/tmp/"
SOLUTION_PATH = BASE_PATH + "solution.txt"


def greedy(g,strategy):
    greedy = nx.greedy_color(g,strategy)
    return greedy

def chromaticNumber(coloring):
    return max(coloring.values()) + 1


def getColoringHEA(listOfNodes, listOfEdges):
    with open(GRAPH_FILE_PATH, "w") as f:
        f.write("p edge " + str(listOfNodes) + " " + str(len(listOfEdges)) + "\n")
        for edge in listOfEdges:
            f.write("e " + str(edge[0]+1) + " " + str(edge[1]+1) + "\n")


    subprocess.run(["./HybridEA", GRAPH_FILE_PATH, "-o", BASE_PATH])

    with open(SOLUTION_PATH, "r") as f:
        numberOfNodes = int(f.readline())
        coloring = []
        for line in f:
            coloring.append(int(line))
        assert len(coloring) == numberOfNodes
        return coloring

