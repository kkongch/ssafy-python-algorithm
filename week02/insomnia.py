tc = int(input())
for test_case in range(1,tc+1):
    N = int(input())
    lst = []
    num = 1
    cnt = 1
    while 1:
        a = N*num
        a = str(a)
        for i in range(len(a)):
            lst.append(a[i])
        new_lst = set(lst)

        if len(new_lst)==10:
            print(f'#{test_case} {a}')
            break
        num += 1



