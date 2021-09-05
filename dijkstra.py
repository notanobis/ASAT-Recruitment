import numpy as np

# Table that shows the connection's weight from i to j
connections = [
    [0, 1, 0, 3, 10],
    [1, 0, 5, 0, 0],
    [0, 5, 0, 2, 1],
    [3, 0, 2, 0, 6],
    [10, 0, 1, 6, 0]
    ]

# The base node that we calculate Dijkstra's algorithm from.
baseNode = 0


weight=[]
unvisited=[]

for i in range(0, len(connections)):
    weight.append(np.infty)
    unvisited.append(i)
weight[baseNode]=0

minimum=0

while len(unvisited) != 0:
    for i in unvisited:
        if minimum>=weight[i]:
            minimum=weight[i]
    i=weight.index(minimum)
    unvisited.remove(i)
    for j in range(0, len(connections)):
        if connections[i][j]!=0:
            weight[j]=min(weight[j], weight[i]+connections[i][j])
    minimum=max(weight)

print("==========================================")
print("Starting from node " + str(baseNode+1) + " :")
print("Minimum distance to other nodes:\n")
print("Node    Distance\n---------------")

for j in range(0, len(connections)):
    print(j+1, "\t\t", weight[j])

print("\n==========================================")
