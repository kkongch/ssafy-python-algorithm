tc = int(input())
for c in range(1,tc+1):
    lst = [list(input()) for _ in range(5)]
    result=[]
    flag=0
    check_lst=[]
    while 1:
        for i in range(5):
            if lst[i]:
                x = lst[i].pop(0)
                result.append(x)
            elif not lst[i] and i not in check_lst:
                check_lst.append(i)
        if len(check_lst)==5:
            break
    print(f'#{c}', end=' ')
    print(*result,sep='')