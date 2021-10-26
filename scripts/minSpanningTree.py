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

g.addEdge(0, 1, -140)
g.addEdge(0, 2, -95)
g.addEdge(0, 3, -180)
g.addEdge(0, 4, -155)
g.addEdge(0, 5, -155)
g.addEdge(0, 6, -120)
g.addEdge(0, 7, -150)
g.addEdge(0, 8, -105)
g.addEdge(0, 9, -155)
g.addEdge(1, 2, -85)
g.addEdge(1, 3, -130)
g.addEdge(1, 4, -145)
g.addEdge(1, 5, -105)
g.addEdge(1, 6, -110)
g.addEdge(1, 7, -140)
g.addEdge(1, 8, -95)
g.addEdge(1, 9, -140)
g.addEdge(2, 3, -105)
g.addEdge(2, 4, -140)
g.addEdge(2, 5, -60)
g.addEdge(2, 6, -205)
g.addEdge(2, 7, -135)
g.addEdge(2, 8, -230)
g.addEdge(2, 9, -100)
g.addEdge(3, 4, -165)
g.addEdge(3, 4, -145)
g.addEdge(3, 4, -110)
g.addEdge(3, 4, -180)
g.addEdge(3, 4, -95)
g.addEdge(3, 4, -145)
g.addEdge(4, 5, -120)
g.addEdge(4, 5, -125)
g.addEdge(4, 5, -175)
g.addEdge(4, 5, -110)
g.addEdge(4, 5, -140)
g.addEdge(5, 6, -85)
g.addEdge(5, 6, -135)
g.addEdge(5, 6, -90)
g.addEdge(5, 6, -120)
g.addEdge(6, 7, -100)
g.addEdge(6, 7, -215)
g.addEdge(6, 7, -105)
g.addEdge(7, 8, -105)
g.addEdge(7, 9, -155)
g.addEdge(8, 9, -110)

 
# Function call
g.KruskalMST()


2 - 8 