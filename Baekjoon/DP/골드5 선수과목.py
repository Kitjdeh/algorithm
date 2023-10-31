#1. N,M을 받는다.
#2. par 관계를 위한 리스트를 만든다.
# par[a] = b / a는 b의 선수과목
#3. 총 M번의 for문을 작성
#4. p,q를받는다.
#5. par[q] = p를 생성
#6. DP[q] +=DP[p] +1

# N,M = map(int,input().split())
# DP = [1]*(N+1)
# par = [[] for i in range(N+1)]
#
# for i in range(M):
#     a,b = map(int,input().split())
#     par[b].append(a)
#
# for i in range(1,N+1):
#     height = 0
#     if par[i]:
#         for j in par[i]:
#             height = max(height,DP[j])
#     DP[i] = height +1
# print(DP[1::])


# while par[a] != 0:
#     DP[b] = max(DP[b],DP[a]+1)
#     a,b = par[a],par[b]
#     print(par[1::])
# print(DP[1::])


# N,M = map(int,input().split())
# DP = [1]*(N+1)
# par = [0]*(N+1)
#
# for i in range(M):
#     a,b = map(int,input().split())
#     par[a] = b
#     while par[a] != 0:
#         DP[b] = max(DP[b],DP[a]+1)
#         a,b = par[a],par[b]
#     print(par[1::])
# print(DP[1::])


N, M = map(int, input().split())

par = [[] for _ in range(N+1)]
DP = [0] * (N+1)
for _ in range(M):
    A, B = map(int, input().split())
    par[B].append(A)

for i in range(1, N+1):
    temp = 0
    if par[i]:
        for pre in par[i]:
            temp = max(temp, DP[pre])
    DP[i] = temp + 1

print(*DP[1:])