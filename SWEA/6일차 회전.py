import sys
sys.stdin = open('6일차 회전.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    print(f'#{tc} {arr[M%N]}')