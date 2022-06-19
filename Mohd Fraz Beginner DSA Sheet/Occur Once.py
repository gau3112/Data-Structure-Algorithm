def occursOnce(a, n):    
    xor_array = 0
    for i in range(len(a)):
        xor_array = xor_array^a[i]
    return xor_array
