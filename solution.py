
def raft(K, weights):
    min = max(weights)

    groups = []
    for i in range(0, K):
        groups.append([])

    gc = 0
    i = 0
    while i < len(weights):
        if weights[i] + sum(groups[gc]) <= min:
            groups[gc].append(weights[i])
            i += 1
        else:
            if gc < K - 1:
                gc += 1
            else:
                minIndex = 0
                for j in range(1, K):
                    if sum(groups[j]) < sum(groups[minIndex]):
                        minIndex = j
                
                groups[minIndex].append(weights[i])
                min = sum(groups[minIndex])
                gc = 0
                i += 1

    maxIndex = 0
    for j in range(1, K):
        if sum(groups[j]) > sum(groups[maxIndex]):
            maxIndex = j

    return sum(groups[maxIndex])
                    


def main():
    N = int(input())
    K = int(input())

    weights = []
    for i in range(0, N):
        weights.append(int(input()))

    weights.sort(reverse=True)
    
    print(raft(K, weights))


main()