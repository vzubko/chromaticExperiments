import matplotlib.pyplot as plt
import graphCreator as graphs
import chromaticNumber as cnum
import expCluster as ec

graph = graphs.clusterGraph(50,14,0.8)


def getChromaticNumber(numberOfNodes, listOfEdges):
    coloring = cnum.getColoringHEA(numberOfNodes, listOfEdges)
    c = max(coloring)
    return c

def graphChromatic(graph):
    c = getChromaticNumber(len(graph.nodes()), graph.edges())
    return c

def getCnumberCluster(graph,listOfNodes):
    chromaticList = []
    for node in range(len(listOfNodes)):
        cNumber = ec.getChromaticWithoutClusterNodes(graph, [listOfNodes[node]])
        chromaticList.append(cNumber)
    return chromaticList

def sortChanges(graph, coefficient, originalChr):
    chromaticList = getCnumberCluster(graph,ec.getNodesOfSameCluster(graph, coefficient))
    reduced = 0
    stayed = 0
    other = 0
    for cnumber in chromaticList:
        if cnumber == originalChr-1:
            reduced += 1
        elif cnumber == originalChr:
            stayed += 1
        else:
            other += 1
    return reduced, stayed, other

def myrange(upto, offset):
    c = offset
    l = []
    while c < upto:
        l.append(c)
        c += 1
    return l

def xfrange(start, stop, step):
    i = 0
    while start + i * step < stop:
        yield start + i * step
        i += 1

def getClusterStatistics(graph, maxCoeff):
    originalChr = graphChromatic(graph)
    reduced = []
    stayed = []
    other = []
    for coeff in range(maxCoeff+1):
        a,b,c = sortChanges(graph,0.1*coeff,originalChr)
        reduced.append(a)
        stayed.append(b)
        other.append(c)
    print(reduced)

    plt.bar([0.1*coeff-.02 for coeff in range(maxCoeff+1)], reduced, width=0.01, color='green')
    plt.bar([0.1*coeff for coeff in range(maxCoeff+1)], stayed, width=0.01, color='yellow')
    plt.bar([0.1*coeff+.02 for coeff in range(maxCoeff+1)], other, width=0.01, color='red')
    plt.gca().set_xticks([0.1*coeff for coeff in range(maxCoeff+1)])
    plt.ylabel('Number of nodes')
    plt.xlabel('Clustering coefficient')
    plt.title('Change in chromatic number as dependence on clustering coefficient')
    plt.show()

print(getClusterStatistics(graph, 10))