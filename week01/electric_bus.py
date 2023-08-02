tc = int(input())
# tc=1
for test_case in range(1,tc+1):
    K,N,M = map(int,input().split())
    # K, N, M = 3,10,5
    charge_cnt = list(map(int,input().split()))
    # charge_cnt = [1,2,3,4,7]
    cnt = 0
    flag = 0
    for i in range(len(charge_cnt)-1):
        if charge_cnt[i+1] - charge_cnt[i] > K or charge_cnt[0]>K or charge_cnt[-1]+K<N:
            flag = 1

    if flag==1:
        print(f'#{test_case} 0')
        continue
    else:
        step = 0
        for i in range(len(charge_cnt)):
            if charge_cnt[1] > K:
                if cnt==0:
                    cnt += 1
                    step = charge_cnt[0]
                    continue

            if i==len(charge_cnt)-1:
                if step+K<N:
                    cnt+=1
                    break
            if step+K>=charge_cnt[i+1]:
                continue
            else:
                cnt+=1
                step = charge_cnt[i]

            if step+K >= N:
                break



        print(f'#{test_case} {cnt}')

