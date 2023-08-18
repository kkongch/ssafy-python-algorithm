tc = int(input())
for test_case in range(1, tc + 1):
    st = input()
    lst = [['.'] * (4 * len(st) + 1) for _ in range(5)]
    num = 0
    for i in range(5):
        if i == 2:
            for k in range(0, 4 * len(st), 4):
                lst[i][k] = '#'
            for k in range(2, 4 * len(st) + 1, 4):
                if len(st) < 2:
                    lst[i][k] = st[0]
                    lst[i][len(st) * 4] = '#'
                else:
                    lst[i][k] = st[num]
                    lst[i][len(st) * 4] = '#'
                    num += 1

        if i % 5 == 0 or i == 4:
            for k in range(len(st)):
                for j in range(2, 4 * len(st), 4):
                    lst[i][j] = '#'
        elif i % 2 == 1:
            for k in range(len(st)):

                for j in range(1, 4 * len(st), 2):
                    lst[i][j] = '#'

    for i in lst:
        print(*i, sep='')