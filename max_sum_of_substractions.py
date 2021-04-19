def alg(arr):
    arr.sort()

    result = []
    for i in range(0, int(len(arr)/2)):
        pair = (arr[i], arr[len(arr)-i-1])
        result.append(pair)
    return result


arr = [5,4,6,10,3,2]
print(alg(arr))