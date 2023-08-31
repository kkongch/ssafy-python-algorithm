from collections import deque
tc = int(input())
for test_case in range(1,tc+1):
    n,m = map(int,input().split())
    q = deque(list(map(int,input().split())))
    for i in range(m):
        x = q.popleft()
        q.append(x)
    print(f'#{test_case} {q[0]}')