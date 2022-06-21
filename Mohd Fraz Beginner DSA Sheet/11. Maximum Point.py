def maximumPoints(n: int, grid: List[List[int]]) -> int:
    grid_sum = 0
    for i in range(len(grid)):
        if i!= len(grid)-1-i:
            grid_sum += grid[i][i] + grid[i][len(grid)-1-i]
        else:
            grid_sum += grid[i][i]
    return grid_sum
