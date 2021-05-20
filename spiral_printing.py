def spiral_printing(A):
    n = len(A)
    m = len(A[0])
    rc,cc = 0,0

    visited = []
    for i in range(0, n):
        buffer = []
        for j in range(0, m):
            buffer.append(False)
        visited.append(buffer)

    for _ in range(0, n*m):
        print(A[rc][cc], end=" ")
        visited[rc][cc] = True

        if cc+1 < m and visited[rc][cc+1] == False:
            cc += 1
        elif rc+1 < n and visited[rc+1][cc] == False:
            rc += 1
        elif cc > 0 and visited[rc][cc-1] == False:
            cc -= 1
        elif rc > 0 and visited[rc-1][cc] == False:
            rc -= 1
            

        
A = [[1], [2]]
spiral_printing(A)