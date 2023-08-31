from collections import deque
tc = int(input())
for test_case in range(1,tc+1):
    n,m = map(int,input().split())
    pizza = list(map(int,input().split()))
    q = deque()
    result = []
    now = n
    for i in range(n):
        q.append([pizza[i],i])
    while q:
        x,idx = q.popleft()
        if x//2==0:
            if len(q) <= n and now < m:
                q.insert(0, [pizza[now], now])
                now += 1
            result.append(idx)
        else:
            q.append([x//2,idx])
    print(f'#{test_case} {result[len(result)-1]+1}')

