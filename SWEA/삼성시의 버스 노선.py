import sys
sys.stdin = open('swea 삼성시의 버스 노선.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    S = [0]*5001
    for i in range(N):
        A,B = map(int,input().split())
        for i in range(A,B+1):
            S[i] +=1
    P = int(input())
    C = [0]*P
    for i in range(P):
        C[i] = int(input())
    print(f'#{tc} ', end='')
    for i in range(P):
        print(S[C[i]], end=' ')
    print()