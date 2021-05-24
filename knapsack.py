def knapsack(V, W, C):
    if C == 0:
        return 0
    
    V.insert(0, None)
    W.insert(0, None)
    n = len(W)
    
    dyn = []
    for _ in range(0, n):
        temp = []
        for _ in range(0, C+1):
            temp.append(0)
        dyn.append(temp)

    for i in range(1, n):
        for k in range(1, C+1):
            if W[i] > k:
                dyn[i][k] = dyn[i-1][k]
            else:
                dyn[i][k] = max(V[i] + dyn[i-1][k-W[i]], dyn[i-1][k])

    V.pop(0)
    W.pop(0)

    return dyn[n-1][C]



print(knapsack([2,3,5,6], [10,12,15,11], 25))