def countNegativeNumbers(mat: List[List[int]]) -> int:
    count = 0
    for i in range(len(mat)):
        start = 0
        end = len(mat[i])-1
        while end>=0 and mat[i][end]<0:
            count+=1
            end-=1
    return count
