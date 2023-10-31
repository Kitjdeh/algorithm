#DP[i][j] = (DP[i-1]
n = int(input())
DP = []
for i in range(n):
    DP.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(len(DP[i])):
        if j ==0:
            DP[i][j] = DP[i-1][0]+DP[i][j]
        elif j == len(DP[i]) -1:
            DP[i][j] = DP[i-1][-1]+DP[i][j]
        else:
            DP[i][j] = DP[i][j]+max(DP[i-1][j-1],DP[i-1][j])
result=0
for i in range(n):
    if DP[n-1][i]>result:
        result = DP[n-1][i]
print(result)