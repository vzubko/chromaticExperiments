import networkx as nx
import matplotlib.pyplot as plt
import graphCreator as graphs
import chromaticNumber as cnum
import time


graph = graphs.clusterGraph(50,30,0.8)

def getChromaticNumber(listOfNodes, listOfEdges):
    coloring = cnum.getColoringHEA(listOfNodes, listOfEdges)
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

print(chromaticChanged(graph))

# start_time = time.time()
#
# print("Finished in %s seconds " % (time.time() - start_time))



# pos = nx.spring_layout(graph, iterations=2000)
# nx.draw(graph, pos, node_color=coloring)
# plt.show()
