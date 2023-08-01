tc = 10
for test_case in range(1, tc + 1):

    b_cnt = int(input())
    b_high = list(map(int, input().split()))

    building_result = 0
    for k in range(len(b_high) - 4):
        max_idx = 0
        MAX = 0
        second = 0
        result = 0
        new_lst = []
        for j in range(k, k + 5):
            new_lst.append(b_high[j])   # new_lst에 5가지 배열만 할당
        for j in range(k, k + 5):   # 최대값의 인덱스 구하기
            if b_high[j]==max(new_lst):
                max_idx = j
        if max_idx == (2 * k + 4) // 2: # 최대값의 인덱스가 배열의 가운데 값이면
            for i in range(5):
                if MAX <= new_lst[i]:
                    second = MAX
                    MAX = new_lst[i]
                elif second< new_lst[i]:
                    second = new_lst[i]
            result = MAX - second
        building_result += result

    print(f'#{test_case} {building_result}')