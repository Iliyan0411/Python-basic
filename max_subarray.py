def max_sub_array(arr):
    max = 0
    temp = 0
    for i in range(0, len(arr)):
        temp += arr[i]
        if temp < 0:
            temp = 0
        elif temp > max:
            max = temp

    return max

    
print(max_sub_array([-3,-4,-1]))

