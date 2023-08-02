tc = 10
for test_case in range(1,tc+1):
    dump_num = int(input())
    box_lst = list(map(int,input().split()))
    for _ in range(dump_num):
        Index_max = box_lst.index(max(box_lst))
        Index_min = box_lst.index(min(box_lst))
        box_lst[Index_max] -=1
        box_lst[Index_min] +=1
    high = max(box_lst)-min(box_lst)
    print(f'#{test_case} {high}')