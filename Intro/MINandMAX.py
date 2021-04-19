
def findHelper(smaller, bigger):
    if len(smaller) == 1:
        return smaller[0], bigger[0]

    new_smaller, new_bigger = [], []
    stat = len(smaller) % 2 == 1

    for i in range(0, len(smaller)-int(stat), 2):
        if smaller[i] < smaller[i+1]:
            new_smaller.append(smaller[i])
        else:
            new_smaller.append(smaller[i+1])
        
        if bigger[i] > bigger[i+1]:
            new_bigger.append(bigger[i])
        else:
            new_bigger.append(bigger[i+1])

    if stat == True:
        last = len(smaller) - 1

        for i in range(0, len(new_smaller)):
            if smaller[last] < new_smaller[i]:
                new_smaller[i] = smaller[last]
            
            if bigger[last] > new_bigger[i]:
                new_bigger[i] = bigger[last]

    return findHelper(new_smaller, new_bigger)



def findMinMax(arr):
    smaller, bigger = [], []

    for i in range(0, len(arr), 2):
        if arr[i] < arr[i+1]:
            smaller.append(arr[i])
            bigger.append(arr[i+1])
        else:
            smaller.append(arr[i+1])
            bigger.append(arr[i])

    return findHelper(smaller, bigger)


def main():
    size = int(input())
    arr = []
    for i in range(0, size):
        arr.append(int(input()))

    min, max = findMinMax(arr)
    print(f"\n({min}, {max})")

main()