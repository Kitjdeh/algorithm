import sys
sys.stdin = open('swea 파리퇴치3.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    p = N + 2*M
    arr = list(([0] * p for i in range(p)))
    for i in range(M,N+M):
            arr[i][M:N+M]=(list(map(int,input().split())))
    max_kill = 0
    for i in range(M,N+M):
        for j in range(M,N+M):
            kill = arr[i][j]
            try:
                for k in range(1,M):
                    kill += arr[i+k][j]
                    kill += arr[i][j+k]
                    kill += arr[i-k][j]
                    kill += arr[i][j-k]
            except IndexError:
                continue
            if max_kill<kill:
                max_kill =kill
    for i in range(M,N+M):
        for j in range(M,N+M):
            kill = arr[i][j]
            try:
                for k in range(1,M):
                    kill += arr[i+k][j+k]
                    kill += arr[i-k][j+k]
                    kill += arr[i-k][j-k]
                    kill += arr[i+k][j-k]
            except IndexError:
                continue

            if max_kill < kill:
                max_kill = kill
    print(f"#{tc} {max_kill}")
