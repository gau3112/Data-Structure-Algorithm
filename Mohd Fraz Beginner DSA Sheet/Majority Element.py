
def findMajorityElement(arr, n):
    index = 1
    
    # For default consider first element as major
    major  = arr[0]
    
    # Keep major count = 1
    count = 1
    
    # Run While Loop till index traverses all element
    while index<len(arr):
        
        # If element at index is equal to major increase the count 
        if arr[index]==major:
            count+=1
            
        # If element is other then major element check for major count if greater than 0 reduce by one else change major to currnt element
        elif count>0:
            count-=1
        else:
            major = arr[index]
            count = 1
        index+=1
    
    # Check for major to confirm (this happens only in case array does'nt have any major element)
    major_count = 0
    for i in arr:
        if i==major:
            major_count+=1
            
    # If count of major element found greater than len(arr)//2 then its a major element return it 
    if major_count>len(arr)//2:
        return major
    else:
        return -1
    return major
