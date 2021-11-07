from collections import defaultdict
 
# Graph representing the full tree 
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary
        # to store graph
 
    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # The main function to construct MST using Kruskal's
        # algorithm
    def KruskalMST(self):
 
        result = []  # This will store the resultant MST
         
        # An index variable, used for sorted edges
        i = 0
         
        # An index variable, used for result[]
        e = 0
 
        # Step 1:  Sort all the edges in
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])
 
        parent = []
        rank = []
 
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
 
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            # If including this edge does't
            #  cause cycle, include it in result
            #  and increment the indexof result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge
 
        minimumCost = 0
        print ("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)
 
# Driver code
g = Graph(10)

g.addEdge(0,1,315)
g.addEdge(0,2,155)
g.addEdge(0,3,560)
g.addEdge(0,4,340)
g.addEdge(0,5,400)
g.addEdge(0,6,320)
g.addEdge(0,7,220)
g.addEdge(0,8,360)
g.addEdge(0,9,360)
g.addEdge(1,2,-70)
g.addEdge(1,3,395)
g.addEdge(1,4,295)
g.addEdge(1,5,215)
g.addEdge(1,6,235)
g.addEdge(1,7,15)
g.addEdge(1,8,275)
g.addEdge(1,9,235)
g.addEdge(2,3,315)
g.addEdge(2,4,175)
g.addEdge(2,5,195)
g.addEdge(2,6,155)
g.addEdge(2,7,-5)
g.addEdge(2,8,215)
g.addEdge(2,9,195)
g.addEdge(3,4,560)
g.addEdge(3,5,540)
g.addEdge(3,6,560)
g.addEdge(3,7,280)
g.addEdge(3,8,560)
g.addEdge(3,9,560)
g.addEdge(4,5,160)
g.addEdge(4,6,-300)
g.addEdge(4,7,160)
g.addEdge(4,8,-780)
g.addEdge(4,9,-780)
g.addEdge(5,6,200)
g.addEdge(5,7,200)
g.addEdge(5,8,240)
g.addEdge(5,9,220)
g.addEdge(6,7,160)
g.addEdge(6,8,-260)
g.addEdge(6,9,-240)
g.addEdge(7,8,220)
g.addEdge(7,9,200)
g.addEdge(8,9,-880)


# """ ConsolidatedMSA Edges
# g.addEdge(0, 1, 2005)
# g.addEdge(0, 2, 5460)
# g.addEdge(0, 3, -260)
# g.addEdge(0, 4, 2285)
# g.addEdge(0, 5, 1520)
# g.addEdge(0, 6, 1535)
# g.addEdge(0, 7, -360)
# g.addEdge(0, 8, -310)
# g.addEdge(0, 9, 5270)
# g.addEdge(0, 10, 1280)
# g.addEdge(0, 11, 1990)
# g.addEdge(1, 2, 5915)
# g.addEdge(1, 3, 635)
# g.addEdge(1, 4, 40)
# g.addEdge(1, 5, 75)
# g.addEdge(1, 6, 90)
# g.addEdge(1, 7, 695)
# g.addEdge(1, 8, 605)
# g.addEdge(1, 9, 6605)
# g.addEdge(1, 10, 1235)
# g.addEdge(1, 11, -55)
# g.addEdge(2, 3, 4150)
# g.addEdge(2, 4, 6135)
# g.addEdge(2, 5, 5750)
# g.addEdge(2, 6, 5725)
# g.addEdge(2, 7, 4170)
# g.addEdge(2, 8, 4120)
# g.addEdge(2, 9, -8980)
# g.addEdge(2, 10, 5930)
# g.addEdge(2, 11, 5860)
# g.addEdge(3, 4,835)
# g.addEdge(3, 5,390)
# g.addEdge(3, 6,365)
# g.addEdge(3, 7,-1250)
# g.addEdge(3, 8,-1540)
# g.addEdge(3, 9,4320)
# g.addEdge(3, 10,850)
# g.addEdge(3, 11,580)
# g.addEdge(4, 5,315)
# g.addEdge(4, 6,310)
# g.addEdge(4, 7,895)
# g.addEdge(4, 8,825)
# g.addEdge(4, 9,6825)
# g.addEdge(4, 10,1475)
# g.addEdge(4, 11,105)
# g.addEdge(5, 6,-795)
# g.addEdge(5, 7,490)
# g.addEdge(5, 8,440)
# g.addEdge(5, 9,6380)
# g.addEdge(5, 10,990)
# g.addEdge(5, 11,120)
# g.addEdge(6, 7,485)
# g.addEdge(6, 8,435)
# g.addEdge(6, 9,6355)
# g.addEdge(6, 10,985)
# g.addEdge(6, 11,95)
# g.addEdge(7, 8,-1460)
# g.addEdge(7, 9,4360)
# g.addEdge(7, 10,990)
# g.addEdge(7, 11,700)
# g.addEdge(8, 9,4250)
# g.addEdge(8, 10,920)
# g.addEdge(8, 11,630)
# g.addEdge(9, 10,6420)
# g.addEdge(9, 11,6530)
# g.addEdge(10, 11,1200)  """

 
# Function call

g.KruskalMST()