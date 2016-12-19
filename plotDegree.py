import matplotlib.pyplot as plt
import graphCreator as graphs
import chromaticNumber as cnum
import expDegree as d

graph = graphs.karateClub()


def getChromaticNumber(numberOfNodes, listOfEdges):
    coloring = cnum.getColoringHEA(numberOfNodes, listOfEdges)
    c = max(coloring)
    return c

def graphChromatic(graph):
    c = getChromaticNumber(len(graph.nodes()), graph.edges())
    return c

def getCnumberDegree(graph,listOfNodes):
    chromaticList = []
    for node in range(len(listOfNodes)):
        cNumber = d.getChromaticWithoutNodes(graph, [listOfNodes[node]])
        chromaticList.append(cNumber)
    return chromaticList

def sortChanges(graph, degree, originalChr):
    chromaticList = getCnumberDegree(graph,d.getNodesOfOneDegree(graph, degree))
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

def getDegreeStatistics(graph, maxDegree):
    originalChr = graphChromatic(graph)
    reduced = []
    stayed = []
    other = []
    for degree in range(maxDegree+1):
        a,b,c = sortChanges(graph,degree,originalChr)
        reduced.append(a)
        stayed.append(b)
        other.append(c)
    plt.bar(myrange(maxDegree+0.5, -0.2), reduced, width=0.2, color='green')
    plt.bar(myrange(maxDegree+0.5, 0), stayed, width=0.2, color='yellow')
    plt.bar(myrange(maxDegree+0.5, 0.2), other, width=0.2, color='red')
    plt.gca().set_xticks(range(maxDegree + 1))
    plt.ylabel('Number of nodes')
    plt.xlabel('Degree')
    plt.title('Change in chromatic number as dependence on degree')
    plt.show()

print(getDegreeStatistics(graph,17))




