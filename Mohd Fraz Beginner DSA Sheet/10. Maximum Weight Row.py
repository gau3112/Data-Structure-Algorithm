def maximumWeightRow(n: int, m: int, mat: List[List[int]]) -> int:
    max_sum = -10000000
    for i in range(len(mat)):
        sum_row = 0
        for j in range(len(mat[i])):
            sum_row += mat[i][j]
        if max_sum<sum_row:
            max_sum = sum_row
    return max_sum
