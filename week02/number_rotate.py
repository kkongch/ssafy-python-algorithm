import copy

tc = int(input())
for test_case in range(1, tc + 1):
    N = int(input())
    rotate_lst = [[] for _ in range(N)]
    result_lst = [['' for _ in range(N)] for _ in range(N)]

    lst = [list(input().split()) for _ in range(N)]
    for _ in range(N):
        for i in range(N):
            for k in range(N):
                result_lst[k][N - i - 1] = lst[i][k]

        for i in range(len(result_lst)):
            rotate_lst[i].append(''.join(result_lst[i]))
        lst = copy.deepcopy(result_lst)
    print(f'#{test_case}')
    for i in range(N):
        for k in range(3):
            print(rotate_lst[i][k], end=' ')
        print()