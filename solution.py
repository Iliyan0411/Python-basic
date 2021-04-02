def sub_set(arr, bit_string):
    result = []

    for i in range(0, len(arr)):
        if bit_string[i] == 1:
            result.append(arr[i])

    return result

def all_sub_sets(arr, bit_string, pos, all_cases):
    if pos == len(arr):
	    all_cases.append(sub_set(arr, bit_string))

    else:
        bit_string[pos] = 0
        all_sub_sets(arr, bit_string, pos + 1, all_cases)
        bit_string[pos] = 1
        all_sub_sets(arr, bit_string, pos + 1, all_cases)

def no_section(arr1, arr2):
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            if arr1[i] == arr2[j]:
                return False

    return True

def sum(arr):
    sum = 0
    for elem in arr:
        sum += elem

    return sum

def raft(K, weights):
    min = -1
    all_ways, bit_string = [], []
    for i in range(0, len(weights)):
        bit_string.append(0)

    all_sub_sets(weights, bit_string, 0, all_ways)

    for i in range(0, len(all_ways)):
        temp = []
        for j in range(0, len(all_ways)):
            if len(temp) > K:
                break
            if i != j:
                for k in range(0, len(temp)):
                    if no_section(temp[k], all_ways[j]):
                        temp.append(all_ways[j])

        max_sum = sum(temp[0])
        for k in range(1, len(temp)):
            if sum(temp[k]) > max_sum:
                max_sum = sum(temp[k])

        if min == -1 or max_sum < min:
            min = max_sum


    return min
                        



def main():
    # N = int(input())
    # K = int(input())

    # weights = []
    # for i in range(0, N):
    #     weight = int(input())
    #     weights.append(weight)

    # weights.sort(reverse=True)
    
    # print(raft(K, weights))

    # all = []
    # all_sub_sets([1], [0,0,0,0,0], 0, all)

    # print(all)


main()