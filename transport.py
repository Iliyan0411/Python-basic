def transport(A, K):
    n = len(A)

    dyn = []
    for _ in range(n+1):
        temp = []
        for _ in range(K+1):
            temp.append(0)
        dyn.append(temp)

    for i in range(0, n+1):
        dyn[i][0] = 0
    for i in range(0, K+1):
        dyn[0][i] = 0

    for i in range(1, n+1):
        for j in range(1, K+1):
            if A[i-1] > K:
                dyn[i][j] = dyn[i-1][j]
            else:
                dyn[i][j] = max(dyn[i-1][j], dyn[i-1][j-A[i-1]] + A[i-1])

    for i in range(0, n+1):
        print(dyn[i])

    return dyn[n][K]


print(transport([2,3,3,9,10], 20))