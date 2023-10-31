# def f(start,goal,price): #출발할 지점 start, 목표지점goal, 현재 까지 비용 price
#     global min_V
#     if start == goal:
#         if min_V > price:
#             min_V = price
#         return
#     elif price >= min_V:
#         return
#     else:
#         for i in range(len(arr[start])):
#             if arr[start][i] != 0:
#                 if  visited[i] ==0:
#                     visited[i] = 1
#                     f(i,goal,price+arr[start][i])
#                     visited[i] = 0
# N = int(input())
# M = int(input())
# arr = [[0]*(N+1) for _ in range(N+1)]
# for _ in range(M):
#     a,b,c= map(int,input().split())
#     arr[a][b] = c
# visited = [0]*(N+1)
# a,b =  map(int,input().split())
# visited[a] =1
# min_V = 100000*N
# f(a,b,0)
# print(min_V)
from sys import stdin
def f(start,goal,price): #출발할 지점 start, 목표지점goal, 현재 까지 비용 price
    global min_V
    if cost[start][goal] !=0 and cost[start][goal] + price < min_V:         #goal 까지 직행값도 확인
        min_V = price + cost[start][goal]
    if start == goal:
        if min_V > price:
            min_V = price
        return
    elif price >= min_V:
        return
    else:
        for i in arr[start]:
            if  visited[i] ==0:
                visited[i] = 1
                f(i,goal,price+cost[start][i])
                visited[i] = 0
N = int(stdin.readline())
M = int(stdin.readline())
arr = [[] for _ in range(N+1)]
cost = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b,c= map(int,stdin.readline().split())
    arr[a].append(b)
    cost[a][b] = c
visited = [0]*(N+1)
a,b =  map(int,stdin.readline().split())
visited[a] =1
min_V = 100000*(N-1)
f(a,b,0)
print(min_V)