def encode(arr):
    count = 1
    res = ""
    res+=arr[0]
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            count+=1
        else:
            res+=str(count)
            res+=arr[i]
            count = 1
    
    res+=str(count)
    return res
