tc = int(input())
for test_case in range(1,tc+1):
    lst = list(map(int,input()))
    cnt = 0
    people = 0
    for i in range(1,len(lst)):
        cnt += lst[i-1]
        if lst[i]==0:
            continue
        if i>cnt:
            people += i-cnt
            cnt += i-cnt

    print(f'#{test_case} {people}')