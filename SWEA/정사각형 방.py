def f(x,y):
    global max_cnt
    global max_num
    cnt = 1
    num = arr[x][y]
    direction = [[1,0],[0,1],[-1,0],[0,-1]]                 #4방향
    ch =1
    di,dj = x,y
    result =[]
    while ch:
        ch =0                                               #리셋 조건
        for i in direction:
            di += i[0]
            dj += i[1]
            if 0<=di<N and 0<=dj<N and arr[di][dj] == num+1:#조건확인
                num +=1
                cnt +=1
                ch = 1                                      #ch값이 존재 하게 하여 while문으로 리셋 조건 충족
                break                                       #di,dj로 기준을 다시 바꿔야 하니 for 문 중단
            else:
                di += -i[0]
                dj += -i[1]
        if ch ==0:
            break
    if max_cnt<cnt:
        max_cnt = cnt
        max_num = arr[x][y]
    elif max_cnt == cnt:
        if arr[x][y] < max_num:
            max_num = arr[x][y]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_cnt=1
    max_num=1
    for i in range(N):
        for j in range(N):
            f(i,j)
    print(f'#{tc} {max_num} {max_cnt}')
