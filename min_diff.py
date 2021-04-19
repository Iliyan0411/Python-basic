
def min_diff(arr, k):
    arr.sort()

    mind = -1
    for i in range(0, len(arr)-k+1):
        currd = arr[i+k-1] - arr[i]
        if currd < mind or mind == -1:
            mind = currd
    return mind 


arr = [50,60,110,20,80]
print(min_diff(arr, 3))