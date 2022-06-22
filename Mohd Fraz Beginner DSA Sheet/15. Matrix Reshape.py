def arrange(n: int, m: int,  mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    if r*c != len(mat)*len(mat[0]):
        return mat
    reshape_mat = [[0 for i in range(c)]for j in range(r)]
    mat_row = 0
    mat_col = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            reshape_mat[mat_row][mat_col] = mat[i][j]
            mat_col+=1
            if mat_col>=c:
                mat_row+=1
                mat_col =0
    return reshape_mat
