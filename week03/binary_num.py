from collections import deque
def change(x,lst):
    q= deque()
    while x!=0:
        if x%2==0:
            q.appendleft(0)
            x//=2
        else:
            q.appendleft(1)
            x//=2
    while len(q)!=4:
        q.appendleft(0)
    lst+=q
tc = int(input())
for c  in range(1,tc+1):
    a,b = input().split()
    lst = []
    dic = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    for i in range(int(a)):
        if 'A'<=b[i]<='F':
            change(dic[b[i]],lst)
        else:
            change(int(b[i]),lst)
    print(f'#{c}', end=' ')
    print(*lst,sep='')
