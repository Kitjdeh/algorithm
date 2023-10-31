import sys
sys.stdin = open("쇠막대기 자르기.txt")
T = int(input())
for tc in range(1,T+1):
    A = input()
    N = len(A)
# 레이저가 나올때 현재 잘릴 수 있게 대기중인 쇠막대기의 갯수 M이 더 생긴다
# 총 쇠 막대기의 개수 t를 더해준다
    M = 0
    cnt=0
    t = 0
    for i in range(N-1):
        if A[i:i+2] == "()":
            cnt += M
        elif A[i:i+2] =="((":
            M +=1
            t +=1
        elif A[i:i+2] == "))":
            M += -1
    print(f"#{tc} {t+cnt}")