tc = int(input())
for test_case in range(1,tc+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    used = [0]*N
    Min = 21e8
    result = []
    def dfs(level):
        global Min
        if sum(result)>Min:
            return
        if level == N:
            if sum(result)<Min:
                Min = sum(result)
                return
            return
        for i in range(N):
            if used[i] ==0:
                used[i] = 1
                result.append(lst[i][level])
                dfs(level+1)
                used[i]=0
                result.pop()
    dfs(0)
    print(f'#{test_case} {Min}')