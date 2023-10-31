import sys
sys.stdin = open("swea 토글.txt")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    a = []
    for i in range(N):
       a.append(list(map(int,input().split())))
    for k in range(1,M+1):
        for i in range(N):
            for j in range(N):
                if M%k == 0:
                    a[i][j] = 0 if a[i][j] == 1 else 1
                else:
                    if (i+j+2) % k ==0:
                        a[i][j] = 0 if a[i][j] == 1 else 1
    sum = 0
    for i in range(N):
        for j in range(N):
            sum += a[i][j]
    print(f'#{tc} {sum}')

