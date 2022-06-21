def swap(n):
    if n==0:
        return 1
    else:
        return 0
      
def getFinalGrid(grid: List[List[int]], n: int) -> List[List[int]]:
    for i in range(len(grid)):
        start = 0
        end = len(grid[i])-1
        while start<=end:
            grid[i][start],grid[i][end] = grid[i][end],grid[i][start]
            if start==end:
                grid[i][start] = swap(grid[i][start])
                break
            grid[i][start] = swap(grid[i][start])
            grid[i][end] = swap(grid[i][end])
            start+=1
            end-=1
    return grid
