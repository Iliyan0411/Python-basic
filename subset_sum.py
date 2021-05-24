def subset_sum(A, S):
    if S == 0:
        return True

    n = len(A)+1
    A.insert(0, None)

    dyn = []
    for _ in range(0,n):
        temp = []
        for _ in range(0, S+1):
            temp.append(False)
        dyn.append(temp)

    for i in range(0, n):
        dyn[i][0] = True

    for i in range(1, n):
        for k in range(1, S+1):
            if A[i] > k:
                dyn[i][k] = dyn[i-1][k]
            else:
                dyn[i][k] = dyn[i-1][k] or dyn[i-1][k-A[i]]

    A.pop(0)
    
    return dyn[n-1][S]




print(subset_sum([1,5,3,7], 4))
print(subset_sum([1,5,3,7], 8))
print(subset_sum([1,5,3,7], 0))
print(subset_sum([1,5,3,7], 14))
print(subset_sum([1,5,3,7], 9))
print(subset_sum([1,5,3,7], 12))