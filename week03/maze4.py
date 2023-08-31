from collections import deque
def bfs(now):
    q = deque()
    q.append(now)
    directy = [1,-1,0,0]
    directx = [0,0,-1,1]
    visited = [[0]*100 for _ in range(16)]
    visited[now[0]][now[1]] = 1
    while q:
        y,x = q.popleft()
        if maze[y][x]==3:
            return 1
        for i in range(4):
            dy = directy[i]+y
            dx = directx[i]+x
            if dy<0 or dx<0 or dy>15 or dx>15:
                continue
            if visited[dy][dx]==1 or maze[dy][dx]==1:
                continue
            visited[dy][dx]=1
            q.append([dy,dx])
    return 0

for test_case in range(1,11):
    tc = int(input())
    maze = [list(map(int,input())) for _ in range(16)]
    for i in range(100):
        if 2 in maze[i]:
            idx = [i,maze[i].index(2)]
            break
    ret = bfs(idx)
    if ret==0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')