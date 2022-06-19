def moveZerosToLeft(arr, n):
    left = n-1
    right = n-1
    while right>=0:
        if arr[right]==0:
            right-=1
        else:
            arr[left],arr[right] = arr[right],arr[left]
            left-=1
            right-=1
