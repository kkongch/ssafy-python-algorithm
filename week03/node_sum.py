tc = int(input())
for test_case in range(1,tc+1):
    m,n,l = map(int,input().split())
    lst = [0]*(m+1)
    for i in range(n):
        a,b = map(int,input().split())
        lst[a] = b
    for i in range(m,-1,-1):
        lst[i//2]+=lst[i]
    print(f'#{test_case} {lst[l]}')
