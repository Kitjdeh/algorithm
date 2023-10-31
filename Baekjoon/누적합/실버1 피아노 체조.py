#1. arr[i] <arr[i+1] -> 실수
#2. 인데스 0부터 누적으로 실수하는 개수를 카운트하여 mis[i] 입력
#3. mis[j]-mis[i] = i~j까지의 실수
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
Q = int(input())
mis = [0]*(N+1)
for i in range(N-1):
    if arr[i] > arr[i+1]:
        mis[i+1] = mis[i]+1
    else:
        mis[i+1] = mis[i]
mis[N] = mis[N-1]
for i in range(Q):
    p,q = map(int,input().split())
    print(mis[q-1]-mis[p-1])