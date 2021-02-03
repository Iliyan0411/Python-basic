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

def printLessPairs (A):
    v = int(input('enter number: '))

    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            if A[i][j] < v: print(f'({i}, {j})')

def magicSquare (A):
    if len(A) == 0: return True

    sum = 0
    for x in A[0]: sum += x

    rowSum, colSum = 0, 0
    for i in range(1, len(A)):
        for j in range(0, len(A[i])):
            rowSum += A[i][j]
            colSum += A[j][i]
        
        if rowSum != sum or colSum != sum: 
            return False
        rowSum, colSum = 0, 0

    mainDiag, secDiag = 0, 0
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            if i == j: mainDiag += A[i][j]
            if i + j == (len(A) - 1): secDiag += A[i][j]

    return mainDiag == sum and secDiag == sum



def main():
    A = [[1,1,1], [1,1,1], [1,1,1]]

    # printMatrix(A)
    # print(MaxInMatrix(A))
    
    # A = EvenToZero(A)
    # print(A)

    # printLessPairs(A)

    # print(magicSquare(A))



main()