def osello(x,y,z):
    directx = [0, 0, -1, 1, 1, -1, 1, -1]
    directy = [1, -1, 0, 0, -1, -1, 1, 1]
    arr[y][x] = z
    for i in range(8):
        cnt = 0
        dy = directy[i]+y
        dx = directx[i]+x
        if z==1:
            while 1:
                cnt += 1
                if dy < 0 or dx < 0 or dy > n - 1 or dx > n - 1:
                    break
                if arr[dy][dx]==1:
                    for j in range(cnt):
                        ddy = directy[i]*j + y
                        ddx = directx[i]*j + x
                        arr[ddy][ddx] = 1
                    break
                if arr[dy][dx]==0:
                    break
                dy+=directy[i]
                dx+=directx[i]

        elif z==2:
            while 1:
                cnt += 1
                if dy < 0 or dx < 0 or dy > n - 1 or dx > n - 1:
                    break
                if arr[dy][dx]==2:
                    for j in range(cnt):
                        ddy = directy[i]*j + y
                        ddx = directx[i]*j + x
                        arr[ddy][ddx] = 2
                    break
                if arr[dy][dx]==0:
                    break
                dy+=directy[i]
                dx+=directx[i]

tc = int(input())
for c in range(1,tc+1):
    n,m = map(int,input().split())
    arr = [[0]*n for _ in range(n)]
    arr[n//2-1][n//2-1],arr[n//2-1][n//2] = 2,1
    arr[n//2][n//2-1],arr[n//2][n//2] = 1,2
    for i in range(m):
        x,y,z = map(int,input().split())
        osello(x-1,y-1,z)
    cnt_1,cnt_2=0,0
    for i in range(n):
        for k in range(n):
            if arr[i][k] == 1:
                cnt_1+=1
            elif arr[i][k]==2:
                cnt_2+=1
    print(f'#{c} {cnt_1} {cnt_2}')

