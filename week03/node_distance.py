from collections import deque
def bfs(start,end):
    global V
    visited = [0]*(V+1)
    q = deque()
    q.append([start,0])
    while q:
        start,cnt = q.popleft()
        if visited[start]==1:
            continue
        if start == end:
            return cnt
        visited[start]=1
        for i in lst[start]:
            q.append([i,cnt+1])
    return 0
tc = int(input())
for test_case in range(1,tc+1):
    V,E = map(int,input().split())
    lst= [[] for _ in range(V+1)]
    for i in range(E):
        s,e = map(int,input().split())
        lst[s].append(e)
        lst[e].append(s)
    start,end = map(int,input().split())
    ret =bfs(start,end)
    print(f'#{test_case} {ret}')