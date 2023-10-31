import sys
sys.stdin= open('분할정복_백트래킹_동철이의 일 분배.txt')
def f(i,N,result):
    global max_V
    if result < max_V:
        return
    elif i == N-1:
        if max_V < result:
            max_V = result
        return
    else:
        for j in range(N):
            if visited[j] ==0:
                visited[j] =1
                f(i+1,N,result*arr[j][i+1])
                visited[j] = 0
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result =1
    max_V = min(arr[0])**N
    visited = [0]*N
    for i in range(N):
        visited[i] =1
        f(0,N,arr[i][0])
        visited[i] = 0
    max_V /= 100**(N-1)
    print(f'#{tc} {max_V:6f}')