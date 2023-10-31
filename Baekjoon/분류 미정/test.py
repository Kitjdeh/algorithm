# def bfs(x,y):
#     for di,dj in direction:
#         ni,nj = x+di,y+dj
#         if 0<=ni<N and 0<=nj<M and maze[ni][nj]==0:
#             maze[ni][nj] = 2
#             bfs(ni,nj)
#
#
# N,M = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# direction = [[1,0],[0,1],[-1,0],[0,-1]]
#
# maze = arr[0:]
# bfs(0,0)
# for i in range(N):
#     print(maze[i])

a = [[1,1]]

b=[1,2]
c = a+[b]
print(c)