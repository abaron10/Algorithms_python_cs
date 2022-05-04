
class Node:
    def __init__(self,name):
        self.name = name
        self.list = []
    
class Graph:
    m = {}

    def __init__(self,cities):
        for citie in cities:
            self.m[citie] = Node(citie)

    def add_edge(self,fromCity,toCity,undir=False):
        self.m[fromCity].list.append(toCity)
        if undir:    
            self.m[toCity].list.append(fromCity)

    def print(self):
        for k,v in self.m.items():
            print(f"{k} ---> {v.list}")

g = Graph([1,2,3,4,5,6])
g.add_edge("Delhi","London")
g.add_edge("NY","London")      
g.add_edge("Delhi","Paris")      
g.add_edge("Paris","NY")      
g.print()