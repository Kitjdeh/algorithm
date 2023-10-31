N,M = map(int,input().split())
L = N-M+1
arr = list([0]*L for i in range(M))
#더미에 쌓인 교과서의 수들 중 가장 큰 max_m을 구한다
#우선 L 길이로 만든 arr을 가로열이 max_m인 행렬로 다시 정리힌다.
max_m = 0
for i in range(M ):
    k = int(input())
    if max_m<k:
        max_m = k
    arr[i][0:k] = list(map(int,input().split()))
a = list([0]*max_m for i in range(M))
for i in range(M):
    for j in range(max_m):
        a[i][j] = arr[i][j]
#가장 긴 행렬에 맞춰진 a를 생성하였음
#stack으로 0이 아닌 숫자들을 세로로 한줄 씩받음
#한줄을 받은 후