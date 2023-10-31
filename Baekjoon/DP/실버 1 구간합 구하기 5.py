# (x1,y1)~ (x2,y2)까지의 합
# = 0,0 에서 x2,y2 전부 합산
# -
# {(0,0에서 x1,y2까지합)+0,0에서 x2,y1까지합 -0,0에서 x1,y1까지합)}
#1. 0~N 까지 N+1길이의 DP배열 만듬
#2.
from sys import stdin
input = stdin.readline
N,M = map(int, input().split())
DP = [[0]* (N+1) for _ in range(N+1)]
for i in range(1,N+1):
    arr = list(map(int,input().split()))
    for j in range(N):
        if j >0:
            arr[j] += arr[j-1]
            DP[i]
        DP[i][j+1] = DP[i-1][j+1]+arr[j]
for i in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    print(DP[x2][y2] - DP[x1-1][y2]-DP[x2][y1-1]+DP[x1-1][y1-1])
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6