import sys
class Graph():
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[[0 for column in range(vertices)]
                    for row in range(vertices)]
    def printMST(self,parent):
        print("edge  \tweight")
        for i in range(1,self.v):
            print(str(parent[i])+"---"+str(i)+"\t"+str(self.graph[i][parent[i]]))
    def minkey(self,key,mst_set):
        min=sys.maxsize
        for v in range(self.v):
            if key[v]<min and mst_set[v] == False:
                min = key[v]
                min_index=v
        return min_index
    def prims(self):
        key = [sys.maxsize]* self.v
        parent=[None]*self.v
        key[0]=0
        mst_set=[False]*self.v
        parent[0]=-1
        for cout in range(self.v):
            u=self.minkey(key,mst_set)
            mst_set[u] = True
            for v in range(self.v):
                if self.graph[u][v]>0 and mst_set[v] == False and key[v]>self.graph[u][v]:
                    key[v]=self.graph[u][v]
                    parent[v] = u
        self.printMST(parent)
g=Graph(5)
g.graph=[[0,2,0,6,0],
         [2,0,3,8,5],
         [0,3,0,0,7],
         [6,8,0,0,9],
         [0,5,7,9,0]]
g.prims()
