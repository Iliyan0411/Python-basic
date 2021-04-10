def partition(arr, low, high): 
	i = (low-1)		 
	pivot = arr[high]

	for j in range(low, high): 
		if abs(arr[j]) <= pivot: 
			i = i+1
			arr[i], arr[j] = arr[j], arr[i] 

	arr[i+1], arr[high] = arr[high], arr[i+1] 
	return (i+1) 

def quickSort(arr, low, high): 
	if len(arr) == 1: 
		return arr 
	if low < high: 
		pi = partition(arr, low, high) 
 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high)


############################################
def close_to_zero(arr):
    quickSort(arr, 0, len(arr)-1)

    min = arr[0] + arr[1]
    for i in range(1, len(arr)-1):
        if abs(arr[i] + arr[i+1]) < abs(min):
            min = arr[i] + arr[i+1]
    return min


arr = [5,4,1,-6,3,2]
print(close_to_zero(arr))
