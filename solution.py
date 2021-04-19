def all_transported(arr):
    for i in range(0, len(arr)):
        if arr[i] == False:
            return False
    return True

def raft(K, weights):
    min = weights[0]

    transported = []
    for i in range(0, len(weights)):
        transported.append(False)

    while True:
        for t in range(0, K):
            sum = 0
            for i in range(0, len(weights)):
                if sum + weights[i] <= min and transported[i] == False:
                    sum += weights[i]
                    transported[i] = True
            
        if all_transported(transported):
            return min
        
        min += 1
        for j in range(0, len(transported)):
            transported[j] = False

                    


def main():
    N = int(input())
    K = int(input())

    weights = []
    for i in range(0, N):
        weights.append(int(input()))

    weights.sort(reverse=True)
    
    print(raft(K, weights))


main()