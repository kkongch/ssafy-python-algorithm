from collections import deque
tc = int(input())
for test_case in range(1,tc+1):
    Day = int(input())
    sell_price = deque(list(map(int,input().split())))
    Sum = 0
    while sell_price:
        max_index = sell_price.index(max(sell_price))
        max_price = max(sell_price)
        if max_index==0:
            sell_price.popleft()
        for i in range(max_index):
            Sum += max_price-sell_price.popleft()

    print(f'#{test_case} {Sum}')