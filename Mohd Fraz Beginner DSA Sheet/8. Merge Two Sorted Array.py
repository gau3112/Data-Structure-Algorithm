def ninjaAndSortedArrays(arr1,arr2,m,n):
    idx_1 = 0
    idx_2 = 0
    while arr1[idx_1]!=0 and idx_2<len(arr2):
        if arr1[idx_1]<=arr2[idx_2]:
            idx_1+=1
        else:
            arr1.insert(idx_1,arr2[idx_2])
            arr1.pop()
            idx_2+=1
            idx_1+=1
    while idx_2<len(arr2):
        arr1.insert(idx_1,arr2[idx_2])
        arr1.pop()
        idx_2+=1
        idx_1+=1
    return arr1
