def abc(level,start):
    Sum=0
    if level==2:
        if path[0]>path[1] or path[1]>N-2 or path[0]>N-3:
            return

        else:
            for i in range(path[0]+1):
                Sum+= M-lst[i].count('W')
            for i in range(path[0]+1,path[1]+1):
                Sum+= M-lst[i].count('B')
            for i in range(path[1]+1,N):
                Sum += M - lst[i].count('R')
            result.append(Sum)
        return

    for i in range(start,N+1):
        if visited[i]==1:
            continue
        path.append(i)
        visited[i]=1
        abc(level+1,start+1)
        visited[i]=0
        path.pop()

tc = int(input())
for test_case in range(1,tc+1):
    N,M = map(int,input().split())
    lst = [list(input()) for _ in range(N)]
    Index=0
    path=[]
    visited = [0]*(N+1)
    result = []
    abc(0,0)
    print(f'#{test_case} {min(result)}')