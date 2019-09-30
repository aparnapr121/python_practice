class Graph:
    def __init__(self):
        self.adj={}
        self.visited=[]


    def addEdge(self,node1,node2):
        if self.adj.get(node1) is None:
            self.adj[node1] = []
        self.adj[node1].append(node2)
        self.visited.append(False)
        #print(self.adj)

    def dfs(self,s):
        print(s)
        self.visited[s] = True
        for x in self.adj[s]:
            #print("x is",x)
            #print(self.adj[s])
            if self.visited[x] == False:
                #print("its false")
                self.dfs(x)
g=Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.dfs(2)







