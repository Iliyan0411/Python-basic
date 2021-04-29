def shortest_paths(maze, N, M, sx, sy):
    for i in range(0, N):
        for j in range(0, M):
            if maze[i][j] != -3:
                maze[i][j] = -1

    q = list()
    count = 0
    
    q.append((maze[sx][sy], sx, sy))
    q.append((-2, -1, -1))
    
    while len(q) != 0:
        curr = q.pop(0)

        if curr[0] == -2 and len(q) == 0:
            break
        elif curr[0] == -2:
            q.append((-2, -1, -1))
            count += 1
        else:
            maze[curr[1]][curr[2]] = count

            if curr[1] - 1 >= 0 and maze[curr[1]-1][curr[2]] == -1:
                q.append((maze[curr[1]-1][curr[2]], curr[1]-1, curr[2]))
            
            if curr[1] + 1 < N and maze[curr[1]+1][curr[2]] == -1:
                q.append((maze[curr[1]+1][curr[2]], curr[1]+1, curr[2]))
            
            if curr[2] - 1 >= 0 and maze[curr[1]][curr[2]-1] == -1:
                q.append((maze[curr[1]][curr[2]-1], curr[1], curr[2]-1))
            
            if curr[2] + 1 < M and maze[curr[1]][curr[2]+1] == -1:
                q.append((maze[curr[1]][curr[2]+1], curr[1], curr[2]+1))

    for i in range(0, N):
        print(maze[i])




maze = [[0,0,0,0],
        [0,-3,0,-3],
        [0,0,-3,0],
        [0,0,0,0]]

shortest_paths(maze, 4, 4, 0, 0)
        
