#I.데이터 수령
#II. 각 물건을 담는 경우의 수를 체크해야함 => 메모제이션 => DP\




N,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12

DP = []
for i in range(N+1):
    DP.append([])
    for j in range(K+1):
        if i == 0 or j ==0:
            DP[i].append(0)
        elif arr[i-1][0] <= j:
            DP[i].append(max(arr[i-1][1]+DP[i-1][j-arr[i-1][0]],DP[i-1][j]))
        else:
            DP[i].append(DP[i-1][j])
print(DP)