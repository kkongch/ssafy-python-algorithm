from collections import deque
def bfs(now):
    global cnt,flag
    visited = [[0]*N for _ in range(N)]
    directy = [1,-1,0,0]
    directx = [0,0,-1,1]
    q = deque()
    q.append(now)
    visited[now[0]][now[1]] = 1
    while q:
        now = q.popleft()
        cnt+=1

        if maze[now[0]][now[1]] == '2':
            flag=1
            break

        for i in range(4):
            dy = directy[i]+ now[0]
            dx = directx[i]+ now[1]

            if dy<0 or dx<0 or dx>N-1 or dy>N-1:
                continue
            if maze[dy][dx]=='1':
                continue
            if visited[dy][dx]==0:
                visited[dy][dx]=1
                q.append([dy, dx])



tc = int(input())
for test_case in range(1,tc+1):
    maze = []
    cnt,flag =0,0
    N = int(input())
    for i in range(N):
        row = list(input())
        if '3' in row:
            y,x = i,row.index('3')
        maze.append(row)

    bfs([y,x])
    if flag == 1:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')