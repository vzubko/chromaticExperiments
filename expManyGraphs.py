import matplotlib.pyplot as plt
import graphCreator as graphs
import chromaticNumber as cnum
import random


def getChromaticNumber(numberOfNodes, listOfEdges):
    coloring = cnum.getColoringHEA(numberOfNodes, listOfEdges)
    c = max(coloring)
    return c

def graphChromatic(graph):
    c = getChromaticNumber(len(graph.nodes()), graph.edges())
    return c

def getChromaticWithoutNodes(graph, listOfNodes):
    edgeList = graph.edges()
    removedEdges = []
    for edge in edgeList:
         if edge[0] not in listOfNodes and edge[1] not in listOfNodes:
            removedEdges.append(edge)
    c = getChromaticNumber(len(graph.nodes()), removedEdges)
    return c

def getCnumber(graph,listOfNodes):
    chromaticList = []
    for node in range(len(listOfNodes)):
        cNumber = getChromaticWithoutNodes(graph, [listOfNodes[node]])
        chromaticList.append(cNumber)
    return chromaticList

def sortChanges(graph, originalChr, listOfNodes):
    chromaticList = getCnumber(graph, listOfNodes)
    print(chromaticList)
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

    print ('reduced:', reduced, 'stayed:', stayed, 'other:', other)
    return reduced, stayed, other

# graph = graphs.randomGraph(8,20)
# print(sortChanges(graph,graphChromatic(graph),graph.nodes()))

def myrange(upto, offset):
    c = offset
    l = []
    while c < upto:
        l.append(c)
        c += 1
    return l


maxCNumber = 200
reduced = []
stayed = []
other = []
countC = []
for i in range(maxCNumber):
    reduced.append(0)
    stayed.append(0)
    other.append(0)


for i in range(150):
    print("graph", i)
    g = graphs.randomGraph(random.randint(50, 150), random.randint(800, 4000))
    originalChr = graphChromatic(g)
    countC.append(originalChr)
    a, b, c = sortChanges(g, originalChr, g.nodes())
    reduced[originalChr] += a
    stayed[originalChr] += b
    other[originalChr] += c

print('reduced:', reduced, 'stayed:', stayed, 'other:', other)

for x in range(maxCNumber):
    total = reduced[x] + stayed[x] + other[x]
    if total > 0:
        reduced[x] = reduced[x]*100/total
        stayed[x] = stayed[x]*100/total
        other[x] = other[x]*100/total


plt.bar(myrange(maxCNumber-0.5, -0.2), reduced, width=0.2, color='green')
plt.bar(myrange(maxCNumber-0.5, 0), stayed, width=0.2, color='yellow')
plt.bar(myrange(maxCNumber-0.5, 0.2), other, width=0.2, color='red')
plt.gca().set_xticks(range(maxCNumber + 1))
plt.ylabel('Percentage of nodes')
plt.xlabel('Chromatic number')
plt.title('Visualizing important nodes by chromatic numbers')
plt.show()
