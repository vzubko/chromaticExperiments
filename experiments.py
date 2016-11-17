

import networkx as nx
import graphCreator
import chromaticNumber

graph = graphCreator.randomGraph(15,21)
print(chromaticNumber.greedy(graph))

