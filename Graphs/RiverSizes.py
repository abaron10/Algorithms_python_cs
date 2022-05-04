def riverSizes(matrix):
    # Write your code here.
    def dfs(r,c):
        matrix[r][c] =0
        lst = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
        vertices = 1
        for row, col in lst:
            if row >= 0 and col >= 0 and row < len(matrix) and col < len(matrix[row]) and matrix[row][col] == 1:
                vertices += dfs(row,col)
        return vertices
    res = []
    rivers = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            pair = 0
            if matrix[r][c] == 1:
                rivers += 1
                pair = dfs(r,c)
                res.append(pair)
    res.sort()
    return res

matrix = [[1,0,0,1,0],[1,0,1,0,0],[0,0,1,0,1],[1,0,1,0,1],[1,0,1,1,0]]
print(riverSizes(matrix))		