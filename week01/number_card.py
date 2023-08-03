tc = int(input())
for test_case in range(1,tc+1):
    card_cnt = int(input())
    card = list(map(int,input()))
    
    cnt_lst = []
    
    for i in range(card_cnt):   # 리스트 요소 중 같은 숫자가 있으면 카운트해서 CNT배열에 넣기
        cnt_lst.append(card.count(card[i]))
    max_cnt = 0
    Index_lst = []
    for i in range(len(cnt_lst)):   # 같은 값이 있는 요소들의 개수가 같은지 확인
        if cnt_lst[i] == max(cnt_lst):
            max_cnt+=1
            Index_lst.append(i)
    if max_cnt >=2: #같은 값이 있는 요소들이 있다면 더 큰 요소 출력
        MAX = 0
        for i in range(len(Index_lst)):
            if MAX<card[Index_lst[i]]:
                MAX = card[Index_lst[i]]
                index_num = Index_lst[i]
            print(f'#{test_case} {card[index_num]} {max(cnt_lst)}')
            break
    else:
        print(f'#{test_case} {card[Index_lst[0]]} {max(cnt_lst)}')
