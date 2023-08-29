from collections import deque
def bfs(now):
    global flag
    q = deque()
    q+=road_lst[now]
    while q:
        now = q.popleft()
        if now == 99:
            flag=1
            break
        if not road_lst[now]:
            continue
        q += road_lst[now]
for _ in range(10):
    tc,road = map(int,input().split())
    lst= list(map(int,input().split()))
    flag = 0
    road_lst = [[] for _ in range(road)]
    while lst:
        road_lst[lst[0]].append(lst[1])
        lst.pop(0)
        lst.pop(0)

    bfs(0)
    if flag == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')