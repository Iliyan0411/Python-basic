def unique(array, l, r):
    arr = []
    for i in range(l, r):
        arr.append(array[i])

    if len(arr) == 1:
        return 1
    if len(arr) == 2:
        if arr[0] == arr[1]:
            return 0
        else:
            return 2

    arr.sort()
    
    counter = 0
    for i in range(1, len(arr)-1):
        if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
            counter += 1

    if arr[0] != arr[1]:
        counter += 1
    if arr[len(arr)-1] != arr[len(arr)-2]:
        counter += 1

    return counter


def main():
    arr = []
    arr = list(map(int, input().split()))

    answers = []
    q = int(input())
    for i in range(0, q):
        l, r = [int(x) for x in input().split()]
        answers.append(unique(arr, l, r))

    print(answers)



main()
