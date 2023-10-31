import sys
sys.stdin = open('swea 가로 세로의 최대합.txt.')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a = list([0]*N for i in range(N))
    for i in range(N):
        a[i] = list(map(int,input().split()))
    max_sum = 0
    wid_sum = []
    hei_sum = []
    for i in range(N):
        sum = 0
        for j in range(N):
            sum +=a[i][j]

        sum += -a[i][j]
        wid_sum.append(sum)
    for i in range(N):
        sum = 0
        for j in range(N):
            sum +=a[j][i]
        hei_sum.append(sum)
    for i in range(N):
        for j in range(N):
            sum = wid_sum[i]+hei_sum[j]
        if max_sum <sum:
            max_sum=sum
    print(wid_sum)
    print(hei_sum)
    print(max_sum)