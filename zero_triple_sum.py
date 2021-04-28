def zero_triple_sum(arr):
    dict = {}
    for i in range(0,len(arr)):
        dict[arr[i]] = 1

    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if (-arr[i]-arr[j]) in dict:
                return True
    return False


arr = [1,5,3,6,0]
print(zero_triple_sum(arr))
