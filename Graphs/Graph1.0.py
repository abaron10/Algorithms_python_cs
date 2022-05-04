

class Graph:
    def __init__(self,v):
        self.v = v
        #dinamyc memory allocation
        self.l = [[] for i in range(v)]

    #node i to node j 
    def addEdge(self,i,j,unidir=False):
        self.l[i].append(j)
        if unidir:
            self.l[j].append(i)
    def printList(self):
        for i in range(len(self.l)):
            print(f"{i} is connected to {self.l[i]}")

    def bfs(self,source,destination=-1):
        visited = set()
        queue = []
        distance = [-1]*self.v
        parent = [-1]* self.v

        if source is None:
            return
        queue.append(source)
        parent[source] = source
        distance[source] = 0 
        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.add(source)
            print(current)
            for neighbor in self.l[current]:
                queue.append(neighbor)
                parent[neighbor] = current
                distance[neighbor] =  distance[current] + 1
        
        #print the shortest distance
        for i in range(self.v):
            print(f"shortest dist to {i} is {distance[i]}")

        if destination != -1:
            temp = destination
            while temp != source:
                print(f"{temp}---")
                temp = parent[temp]

    
g = Graph(7)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(3,5)
g.addEdge(5,6)
g.addEdge(4,5)
g.addEdge(0,4)
g.addEdge(3,4)
g.bfs(1)
