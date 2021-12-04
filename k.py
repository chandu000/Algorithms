class Graph:
    def __init__(self, vertices):
        self.V=vertices
        self.graph=[]
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    def find(self,parent,a):
        if parent[a] == a:
            return a
        return self.find(parent, parent[a])
    def union(self, parent, rank,x,y):
        xadj = self.find(parent, x)
        yadj = self.find(parent, y)
        if rank[xadj]<rank[yadj]:
            parent[xadj] = yadj
        elif rank[xadj]>rank[yadj]:
            parent[yadj]=xadj
        else:
            parent[yadj] = xadj
            rank[xadj]+=1           
    def kMST(self):
        mst_res = []
        se,fe=0,0 #se is used to iterate sorted edges,fe is used to iterate final edges of minimum spanning 
        self.graph = sorted(self.graph,key=lambda item: item[2],reverse = False)
        p =[] #parent array
        r =[] #rank array
        for n in range(self.V):
            p.append(n)
            r.append(0)
        while fe< self.V-1:
            h=self.graph[se]
            u=h[0]
            v=h[1]
            w=h[2]
            se+=1
            x = self.find(p, u)
            y = self.find(p, v)
            if x!=y:
                fe+=1
                mst_res.append([u,v,w])
                self.union(p,r,x,y)
        min=0
        print("mst is:")
        for u, v, weight in mst_res:
            min+=weight
            print("%d -- %d == %d" %(u,v,weight))
        print("cost:"+str(min))
g = Graph(50)
g.addEdge(0,1,5)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,1,10)
g.addEdge(1,3,15)
g.addEdge(2,3,4)
g.addEdge(3,3,1)
g.addEdge(4,3,2)
g.addEdge(5,4,4)
g.addEdge(6,4,5)
g.addEdge(7,4,6)
g.addEdge(8,5,1)
g.addEdge(3,4,1)
g.addEdge(9,3,5)
g.addEdge(10,8,4)
g.addEdge(11,10,3)
g.addEdge(12,13,5)
g.addEdge(13,14,10)
g.addEdge(10,12,5)
g.addEdge(15,14,4)
g.addEdge(16,14,20)
g.addEdge(17,15,25)
g.addEdge(20,19,26)
g.addEdge(19,21,7)
g.addEdge(21,22,5)
g.addEdge(22,0,3)
g.addEdge(28,0,7)
g.addEdge(16,26,5)
g.addEdge(19,28,6)
g.addEdge(20,27,0)
g.addEdge(25,29,7)
g.addEdge(30,31,4)
g.addEdge(31,32,17)
g.addEdge(32,33,20)
g.addEdge(33,34,21)
g.addEdge(34,35,31)
g.addEdge(35,36,21)
g.addEdge(36,37,2)
g.addEdge(37,38,5)
g.addEdge(38,39,21)
g.addEdge(39,40,20)
g.addEdge(40,41,202)
g.addEdge(41,42,2)
g.addEdge(42,43,5)
g.addEdge(43,44,6)
g.addEdge(45,46,11)
g.addEdge(46,47,34)
g.addEdge(47,48,32)
g.addEdge(49,0,21)
g.addEdge(41,44,2)
g.addEdge(44,32,77)
g.addEdge(34,44,202)
g.addEdge(32,7,5)
g.addEdge(31,2,4)
g.addEdge(30,4,5)
g.addEdge(29,22,6)
g.addEdge(23,26,78)
g.addEdge(46,36,212)
g.addEdge(37,17,14)
g.kMST()
