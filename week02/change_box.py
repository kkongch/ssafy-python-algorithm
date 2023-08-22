tc = int(input())
for test_case in range(1,tc+1):
    N,Q = map(int,input().split())
    lst = [0]*(N+1)

    for i in range(1,Q+1):
        L,R =map(int,input().split())
        for k in range(L,R+1):
            lst[k] = i

    print(f'#{test_case} ',end='')
    for i in range(1,len(lst)):
        print(lst[i],end =' ')
    print()