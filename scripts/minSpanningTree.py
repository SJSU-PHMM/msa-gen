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

#zbot
g.addEdge(0,1,4635)
g.addEdge(0,2,4525)
g.addEdge(0,3,-9520)
g.addEdge(0,4,4585)
g.addEdge(0,5,3485)
g.addEdge(0,6,-10315)
g.addEdge(0,7,-10360)
g.addEdge(0,8,4795)
g.addEdge(0,9,-9505)
g.addEdge(1,2,920)
g.addEdge(1,3,5195)
g.addEdge(1,4,-2560)
g.addEdge(1,5,2480)
g.addEdge(1,6,4640)
g.addEdge(1,7,4635)
g.addEdge(1,8,1330)
g.addEdge(1,9,5150)
g.addEdge(2,3,5105)
g.addEdge(2,4,870)
g.addEdge(2,5,2510)
g.addEdge(2,6,4530)
g.addEdge(2,7,4525)
g.addEdge(2,8,140)
g.addEdge(2,9,5040)
g.addEdge(3,4,5085)
g.addEdge(3,5,3945)
g.addEdge(3,6,-9535)
g.addEdge(3,7,-9520)
g.addEdge(3,8,5255)
g.addEdge(3,9,-10745)
g.addEdge(4,5,2430)
g.addEdge(4,6,4610)
g.addEdge(4,7,4585)
g.addEdge(4,8,1320)
g.addEdge(4,9,5060)
g.addEdge(5,6,3490)
g.addEdge(5,7,3485)
g.addEdge(5,8,2480)
g.addEdge(5,9,4000)
g.addEdge(6,7,-10315)
g.addEdge(6,8,4800)
g.addEdge(6,9,-9520)
g.addEdge(7,8,4795)
g.addEdge(7,9,-9505)
g.addEdge(8,9,5250)

# g.addEdge(0,1,0)
# g.addEdge(0,2,-60)
# g.addEdge(0,3,-60)
# g.addEdge(0,4,-20)
# g.addEdge(0,5,-60)
# g.addEdge(0,6,-20)
# g.addEdge(0,7,-20)
# g.addEdge(0,8,-80)
# g.addEdge(0,9,-45)
# g.addEdge(1,2,-40)
# g.addEdge(1,3,-60)
# g.addEdge(1,4,0)
# g.addEdge(1,5,-20)
# g.addEdge(1,6,-200)
# g.addEdge(1,7,-40)
# g.addEdge(1,8,-20)
# g.addEdge(1,9,-25)
# g.addEdge(2,3,-80)
# g.addEdge(2,4,-80)
# g.addEdge(2,5,-120)
# g.addEdge(2,6,-40)
# g.addEdge(2,7,-60)
# g.addEdge(2,8,-60)
# g.addEdge(2,9,-65)
# g.addEdge(3,4,-80)
# g.addEdge(3,5,-80)
# g.addEdge(3,6,-20)
# g.addEdge(3,7,-60)
# g.addEdge(3,8,-60)
# g.addEdge(3,9,-165)
# g.addEdge(4,5,-20)
# g.addEdge(4,6,-60)
# g.addEdge(4,7,-120)
# g.addEdge(4,8,-40)
# g.addEdge(4,9,-45)
# g.addEdge(5,6,0)
# g.addEdge(5,7,-20)
# g.addEdge(5,8,-20)
# g.addEdge(5,9,-65)
# g.addEdge(6,7,-100)
# g.addEdge(6,8,-20)
# g.addEdge(6,9,15)
# g.addEdge(7,8,-40)
# g.addEdge(7,9,-5)
# g.addEdge(8,9,-25)


 
# Function call

g.KruskalMST()