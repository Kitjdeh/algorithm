import sys
sys.stdin= open('분할정복_백트래킹_동철이의 일 분배.txt')


def f(i, p):
    global result
    if p <= result:
        return
    elif i == N:
        result = p if p >= result else result
    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                f(i + 1, p * arr[i][j] / 100)
                visited[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 0
    f(0, 100)
    print(f'#{tc} {result:.6f}')