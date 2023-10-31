import sys
sys.stdin = open('파리 퇴치.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    a=[0]*N
    max_kill = 0
    for i in range(N):
        a[i] = list(map(int,input().split()))       #리스트 수령
    for i in range(N-M+1):                          #파리채 길이에 맞게 범위 설정
        for j in range(N-M+1):
            kill = 0
            for t in range(0,M):
                for p in range(0,M):
                    kill += a[i+p][j+t]             #M*M의 박스 존으로 sum
            if max_kill < kill:
                max_kill = kill
    print(f"#{tc} {max_kill}")