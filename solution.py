
def raft(K, weights):
    total = 0
    for w in weights:
        total += w

    transported = []
    for i in range(0, len(weights)):
        transported.append(False)

    min_capacity = int(total / K) + 1

    counter = 0
    for i in range(0, K):
        temp = 0
        for j in range(0, len(weights)):
            if transported[j] == False and temp + weights[j] <= min_capacity:
                temp += weights[j]
                transported[j] = True
        
        counter += 1

    return min_capacity





def main():
    N = int(input())
    K = int(input())

    weights = []
    for i in range(0, N):
        weight = int(input())
        weights.append(weight)

    weights.sort(reverse=True)
    
    print(raft(K, weights))


main()