#1. idx0 부터 누적으로 합을 더한 DP값을 만든다.
#2. DP[k] -DP[k-1] = k번까지 더한수 - (k-1)번까지 더한 수
N,M = map(int,input().split())
arr = list(map(int,input().split()))
DP = [0]*(N+1)
for i in range(N):
    DP[i+1] =DP[i]+arr[i]
for _ in range(M):
    i,j = map(int,input().split())
    if i ==j:
        print(arr[i-1])
    else:
        print(DP[j]-DP[i-1])