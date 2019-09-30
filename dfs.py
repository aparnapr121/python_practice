class Graph:
    def __init__(self):
        self.adj={}

    def addEdge(self,node1, node2):
        if self.adj.get(node1) is None:
            self.adj[node1] = []
        self.adj[node1].append(node2)

    def _bfs_util(self,s, visited):
        if visited[s] == False:
            visited[s] = True
        print(s)
        #print(visited)
        neigh_list=[]
        #print(self.adj[s])
        for x in self.adj[s]:
            #print("x is",x)
            if visited[x] == False:
                #print(x)
                visited[x]=True
                neigh_list.append(x)
        #neigh_list_len = len(neigh_list)
        for x in neigh_list:
            self._bfs_util(x,visited)





    def bfs(self,s):
        visited = [False] * len(self.adj)
        print(self.adj)
        self._bfs_util(s,visited)

g=Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.bfs(2)
