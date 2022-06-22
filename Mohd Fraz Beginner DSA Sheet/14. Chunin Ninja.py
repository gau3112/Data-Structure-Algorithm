def chuninNinja(n: int, m: int, arr: List[int]) -> List[int]:
    chunin = []
    min_row = [+10000000 for i in range(n)]
    max_col = [-10000000 for i in range(m)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if min_row[i]>arr[i][j]:
                min_row[i] = arr[i][j]
            if max_col[j]<arr[i][j]:
                max_col[j] = arr[i][j]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if max_col[j] == arr[i][j] and  min_row[i]==arr[i][j]:
                chunin.append(arr[i][j])
    
    return chunin
