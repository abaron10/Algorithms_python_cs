
from collections import defaultdict
class Graph():

    def defValue():
        return None

    class Node():
        def __init__(self,label):
            self.label = label

        def __repr__(self):
            return self.label

    
    nodes = defaultdict(defValue)
    adjencyList = defaultdict(defValue)

    def addNode(self,label):
        node = self.Node(label)
        self.nodes[label] = node
        self.adjencyList[node] = []

    def addEdge(self,fromN,toN):
        if (fromN or toN) not in self.nodes: 
            raise Exception
        toNode = self.nodes[toN]
        fromNode = self.nodes[fromN]

        self.adjencyList[fromNode].append(toNode)

    def removeNode(self,label):
        if label in self.nodes:
            node = self.nodes[label]
            for item in self.adjencyList:
                if node in self.adjencyList[item]:
                    self.adjencyList[item].remove(node)
            del self.adjencyList[node]
            del self.nodes[label]
        return

    def removeEdge(self,fromN,toN):
        if (fromN or toN) not in self.nodes: 
            raise Exception
        toNode = self.nodes[toN]
        fromNode = self.nodes[fromN]
        self.adjencyList[fromNode].remove(toNode)
    
    def print(self):
        for item in self.adjencyList.keys():
            targets = self.adjencyList[item]
            if targets:
                print(f"{item} is connected to {targets}")

    #traversals algoritms
    #DFS busca en los nodos que sigue (adjecy list)
    #por cada uno lo manda a la funcion de traverse y por ende a visitar
    #Es bueno para edge classification
        #1. Tree Edges: Parent de un unvisited node (Visitamos un nuevo vertex por medio de este)
        #2. Forward Edges: Va de un nodo a un descendiente
        #3. Backward Edges: Cuando un nodo va a un ancestro mas arriba
        #4. Cross Edges: Cuando no es un ancestro o descendiente (primos)
    def depthFirstSearchRecursive(self,root):
        #set is like a hashtable but stores only the keys
        node = self.nodes.get(root)
        if node is None:
            return
        self.traverseDepthFirst(self.nodes[root],set())

    def traverseDepthFirst(self,root,visited):
        print(root)
        #agregamos el root al set de visitados 
        visited.add(root)
        for node in self.adjencyList[root]:
            if node not in visited:
                self.traverseDepthFirst(node, visited)

    def depthFirstSearchIterative(self,root):
        #set is like a hashtable but stores only the keys
        # push(root)
        # while(stack is not empty)
        #    current = pop()
        #    visit(current)
        #    push each unvisited neighbout 
        node = self.nodes.get(root)
        if node is None:
            return

        stack = []
        visited = set()
        stack.append(node)

        while(stack):
            current = stack.pop()

            if current in visited:
                continue
            print(current)
            visited.append(current)

            for neighbor in self.adjencyList[current]:
                if node not in visited:
                    stack.append(neighbor)

    #breadth first search iterative
    #BFS es bueno para encontrar el camino mas corto 

    def breadthSearchFirst(self,root):
        visited = []
        queue = []
        node = self.nodes.get(root)
        if node is None:
            return
        queue.append(node)
        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.append(current)
            print(current)
            self.adjencyList[current].sort(key=lambda x:x.label,reverse=False)
            for neighbor in self.adjencyList[current]:
                queue.append(neighbor)

    def topologicalSort(self):
        stack = []
        visited = set()
        sort = []
        #La idea aca es recorrer con este ciclo todos los nodos para asegurarnos que la recorrimos
        # toda. 
        for node in self.nodes.values():
            if node not in visited:
                self.topologicalSorting(node,visited,stack)
        while stack:
            sort.append(stack.pop().label)
        return sort

    def topologicalSorting(self,node,visited,stack):
        visited.add(node)
        for neighbor in self.adjencyList[node]:
            if neighbor not in visited:
                self.topologicalSorting(neighbor,visited,stack)
        stack.append(node)

    #Como detectar un cycle ??
    #all --- visiting ---- visited
    #Con un DFS 
    def hasCycle(self):
        #Se copia a un set todos los nodos
        allNodes = set(self.nodes.values())
        #Nodos que se estan visitando / si se encuentras dos iguales hay un ciclo (back-edge).
        visiting = set()
        #Si ya no tiene mas vecinos se mueve aca 
        visited  = set()
        while allNodes:
            current = next(iter(list(allNodes)))
            if self.hasCycleB(current,allNodes,visiting,visited):
                return True
        return False

    def hasCycleB(self,node,all,visiting,visited):
        all.remove(node)
        visiting.add(node)
        for neighbor in self.adjencyList[node]:
            if neighbor in visited:
                continue
            if neighbor in visiting:
                return True
            if self.hasCycleB(neighbor,all,visiting,visited):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

g = Graph()
#Cycle detection
# g.addNode("A")
# g.addNode("B")
# g.addNode("C")
# g.addEdge("A","B")
# g.addEdge("B","C")
# g.addEdge("A","C")
# print(g.hasCycle())

#Topological sorting
g.addNode("X")
g.addNode("A")
g.addNode("B")
g.addNode("P")
g.addEdge("X","A")
g.addEdge("X","B")
g.addEdge("A","P")
g.addEdge("B","P")
print(g.topologicalSort())

# g.addNode("A")
# g.addNode("B")
# g.addNode("C")
# g.addNode("D")

# g.addEdge("A","B")
# g.addEdge("B","D")
# g.addEdge("D","C")
# g.addEdge("A","C")
# g.breadthSearchFirst("A")



