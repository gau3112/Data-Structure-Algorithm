def printPascal(n:int):
    pascal_triangle = [[1 for i in range(x+1)]for x in range(n)]
    for i in range(len(pascal_triangle)):
        for j in range(len(pascal_triangle[i])):
            if j==0 or j==i:
                pass
            else:
                pascal_triangle[i][j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]
    return pascal_triangle
