def beautifulIndex(N: int, A: List[int]) -> int:
    array_sum = sum(A)
    left_sum = 0
    value = 0
    for i in range(0,len(A),1):
        if i==0 and left_sum==array_sum-A[0]:
            return 1
        if i==len(A)-1 and left_sum==0:
            return len(A)
        if left_sum == array_sum-left_sum-A[i]:
            return i+1
        left_sum += A[i]
    else:
        return -1
