def thief(A):
    n = len(A)
    if n == 1:
        return A[0]

    dyn = [0 for _ in range(n)]
    taken = [False for _ in range(n)]

    dyn[0] = A[0]
    dyn[1] = max(A[0], A[1])

    for i in range(2, n):
        dyn[i] = max(dyn[i-1], dyn[i-2] + A[i])

    taken[0] = True
    if A[1] > A[0]:
        taken[1] = True

    for i in range(2, n):
        if dyn[i-2]+A[i] > dyn[i-1]:
            taken[i] = True
    
    i = 0
    while i < n:
        if taken[i]:
            print(A[i], end=" ")
            i += 1
        i += 1

    print("")
    return dyn[n-1]


print(thief([1,5,7,8,10]))