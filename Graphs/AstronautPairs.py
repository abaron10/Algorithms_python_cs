

def journeyToMoon(n, astronaut):
    # Write your code here
    graph = [[] for i in range(n)]
    for x,y in astronaut:
        graph[x].append(y)
        graph[y].append(x)
        
    visited = [False]*n
    pairs = n*(n-1)//2
    
    def dfs(u,graph,visited):
        visited[u] = True
        vertices = 1
        for v in graph[u]:
            if visited[v] == False:
                vertices += dfs(v,graph,visited)
        return vertices
    
    for v in range(n):
        if visited[v] == False:
            n_persons = dfs(v,graph,visited)
            pairs -= n_persons * (n_persons-1)//2
    return pairs

print(journeyToMoon(5,[[0,1],[2,3],[0,4]]))