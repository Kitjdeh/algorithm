import sys
sys.stdin = open("완전검새_그리디_5189전자키트.txt")
def bfs(st,N,c,dis):
    global min_dis
    if c == N-1:
        dis += arr[st][0]
        if min_dis >dis:
            min_dis = dis
        return
    else:
        visited[st] = 1
        for i in range(1,N+1):
            if visited[i] == 0:
                bfs(i,N,c+1,dis+arr[st][i-1])
        visited[st] = 0
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[] for i in range(N+1)]
    way = [[100**N] for _ in range(N+1)]
    for i in range(1,N+1):
        arr[i] = list(map(int,input().split()))
    visited = [0]*(N+1)
    min_dis = 100*(N+2)
    bfs(1,N,0,0)
    print(f'#{tc} {min_dis}')