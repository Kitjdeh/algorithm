def f(x,y,c):
    direction = [[-1,0],[1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]     #8가지 방향
    if c == 1:                                                              #색깔에 따른 적,아군 구분
        pos = 'B'
        tar = 'W'
        arr[x][y] = 'B'
    else:
        pos = 'W'
        tar = 'B'
        arr[x][y] = 'W'

    for i in direction:                                                     #8방향중 하나들 잡아서
        di,dj = x,y
        result = []
        for _ in range(N+1):                                                #N만큼 계속 더한다(=이동시킨다)
            di += i[0]
            dj += i[1]
            if di<0 and di>N-1 and dj<0 and dj>N-1:                         #판 밖으로 나가면 break
                break
            elif 0<=di<=N-1 and 0<=dj<=N-1 and arr[di][dj]==tar:            #다른 색깔이면 좌표 저장
                a,b = di,dj
                result.append([a,b])
            elif 0<=di<=N-1 and 0<=dj<=N-1 and arr[di][dj] ==pos:           #같은 색깔이 나오면 저장한 좌표를 다 같은 색으로 변환
                for j in result:
                    arr[j[0]][j[1]] = pos
                break
            elif 0<=di<=N-1 and 0<=dj<=N-1 and arr[di][dj] ==0:             #공백이 나오면 저장한 값 다 리셋시킴
                result =[]
                break


T= int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [[0]*N for i in range(N)]
    arr[N//2][N//2],arr[(N//2)-1][(N//2)-1] = 'W','W'
    arr[(N//2) - 1][N // 2], arr[N//2][(N //2) - 1] = 'B', 'B'
    for i in range(M):
        x,y,c = map(int,input().split())
        f(x-1,y-1,c)
    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='W':
                white +=1
            elif arr[i][j]=='B':
                black +=1
    print(f'#{tc} {black} {white}')