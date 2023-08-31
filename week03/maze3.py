from collections import deque
def bfs(now):
    q = deque()
    cnt=0
    directx = [-1,1,0,0]
    directy = [0,0,1,-1]
    q.append(now+[0])
    visited[now[0]][now[1]]=1
    while q:
        y,x,cnt= q.popleft()
        if lst[y][x]==2:
            return cnt

        for i in range(4):
            dy = directy[i]+y
            dx = directx[i]+x
            if dy<0 or dx<0 or dy>n-1 or dx>n-1:
                continue
            if visited[dy][dx]==1:
                continue
            if lst[dy][dx]==1:
                continue
            visited[dy][dx]=1
            q.append([dy,dx, cnt+1])

    return 0

tc = int(input())
for test_case in range(1,tc+1):
    n = int(input())
    lst = [list(map(int,input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        if 3 in lst[i]:
            idx = [i,lst[i].index(3)]
    ret = bfs(idx)
    if ret==0:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} {ret-1}')

