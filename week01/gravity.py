tc = int(input())

for test_case in range(1, tc+1):
    row = int(input())
    high = list(map(int,input().split()))
    drop_lst = []
    MAX = 0

    num = 1
    for i in range(row):
        cnt = 0
        for k in range(num,row):
            if high[i]!=0:
                if high[i]>high[k] or high[k]==0:
                    cnt+=1
        num+=1
        drop_lst.append(cnt)

    for i in range(len(drop_lst)):
        if MAX<drop_lst[i]:
            MAX = drop_lst[i]
        
    print(f'#{tc} {MAX}')