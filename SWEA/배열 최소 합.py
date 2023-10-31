import sys
sys.stdin = open('배열 최소합.txt')
T = int(input())
def f(i,N):
    global minx
    if i == N:
        a = 0
        for k in range(N):
            a += arr[k][P[k]]
        if minx > a :
            minx = a
    else:
        for j in range(i,N):
            P[i],P[j] = P[j],P[i]
            f(1+i,N)
            P[i], P[j] = P[j], P[i]

def f2(i,s,N):          #i행, s = i-1행가지의 합, N총 행수
    global minx
    if i == N:
        if minx > s :
            minx = s
    elif minx < s:
        return
    else:
        for j in range(i,N):
            P[i],P[j] = P[j],P[i]
            f2(1+i,s+arr[i][P[i]],N)
            P[i], P[j] = P[j], P[i]
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    P = list(i for i in range(N))
    minx =1000
    f2(0,0,N)
    print(f'#{tc} {minx}')
