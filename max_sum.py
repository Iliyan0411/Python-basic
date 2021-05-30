def max_sum(A, B, C):
    n = len(A)
    dyn = []
    for _ in range(3):
        dyn.append([0 for _ in range(n)])
    
    dyn[0][0] = A[0]
    dyn[1][0] = B[0]
    dyn[2][0] = C[0]

    for i in range(1, n):
        dyn[0][i] = A[i] + max(dyn[1][i-1], dyn[2][i-1])
        dyn[1][i] = B[i] + max(dyn[0][i-1], dyn[2][i-1])
        dyn[2][i] = C[i] + max(dyn[0][i-1], dyn[1][i-1])
        
    
    return max(dyn[0][n-1], dyn[1][n-1], dyn[2][n-1])


print(max_sum([2,3,5,1,8,7,6], [6,9,8,0,5,9,7], [4,1,2,8,4,2,5]))