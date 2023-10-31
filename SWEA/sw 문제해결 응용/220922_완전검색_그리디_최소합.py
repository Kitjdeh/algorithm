import sys
sys.stdin = open("220922_완전검색_그리디_최소합.txt")
def bfs(x,y,n,c):
    if x== n-1 and y ==n-1:             #종료 조건
        ord.append(c)                   #ord에 투입
        return ord
    else:
        if x ==n-1:
            if c+arr[x][y+1] < way[x][y+1]:
                way[x][y+1] = c+arr[x][y+1]
                bfs(x,y+1,n,c+arr[x][y+1])  #x값이 최대면 y쪽 으로 1개만 파생
        elif y ==n-1:
            if c + arr[x+1][y] < way[x+1][y]:
                way[x+1][y] = c + arr[x+1][y]
                bfs(x+1,y,n,c+arr[x+1][y])  #y값이 최대면 x쪽으로 1개만 파생
        else:
            if c + arr[x][y + 1] < way[x][y + 1]:
                way[x][y + 1] = c + arr[x][y + 1]
                bfs(x, y + 1, n, c + arr[x][y + 1])
            if c + arr[x+1][y] < way[x+1][y]:
                way[x+1][y] = c + arr[x+1][y]
                bfs(x+1,y,n,c+arr[x+1][y])  #y값이 최대면 x쪽으로 1개만 파생
    return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    way = [[20*N]*N for _ in range(N)]
    ord = []
    result = 20*N
    bfs(0,0,N,arr[0][0])
    for i in range(len(ord)):
        if result > ord[i]:
            result = ord[i]
    print(f'#{tc} {result}')