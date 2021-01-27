def printMatrix(A):
    for row in A:
        print(row)

def MaxInMatrix(A):
    max = A[0][0]

    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            if A[i][j] > max: max = A[i][j]

    return max

def EvenToZero(A):
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            if A[i][j] % 2 == 0: 
                A[i].pop(j)
                

    return A




def main():
    A = [[1,2,3], [4,5,6], [7,8,9]]

    # printMatrix(A)
    # print(MaxInMatrix(A))
    
    A = EvenToZero(A)
    print(A)



main()