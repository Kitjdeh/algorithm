import sys
sys.setrecursionlimit(10**6)
direction = {                               #방위
    0:[-1,0],
    1:[0,1],
    2:[1,0],
    3:[0,-1]
}
dir_change = [3,0,1,2]                      #왼쪽방향 볼때 차이들
N, M = map(int,input().split())
r,c,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
result = 0
rotate = 0
# clean(r,c,d)
visited[r][c] = 1
result += 1
d = dir_change[d]
rotate += 1  # 왼쪽으로 돌아봐야 하니 +1
ni, nj = r, c
while True:
    ni, nj = r + direction[d][0], c + direction[d][1]
    if visited[ni][nj] == 0 and arr[ni][nj] == 0:  # 2-1번
        rotate = 0
        r, c = ni, nj
        visited[r][c] = 1
        result += 1
        d = dir_change[d]
        rotate += 1
    elif arr[ni][nj] == 1 and rotate < 4:  # 2-2 벽에막힐 경우
        d = dir_change[d]
        rotate += 1
    elif visited[ni][nj] == 1 and rotate < 4:  # 2-2 방문했을경우
        d = dir_change[d]
        rotate += 1
    elif rotate == 4 and arr[r - direction[d][0]][c - direction[d][1]] == 0:                      #뒤로 갈 수 있게 범위가 0~n-1이고 벽이 아닐때
        r, c = r - direction[d][0], c - direction[d][1]
        rotate = 0
    elif rotate == 4:
        break
print(result)
# def clean(r,c,d):
#     global result
#     global rotate
#     if visited[r][c] == 0:
#         visited[r][c] = 1
#         result +=1
#     d = dir_change[d]
#     rotate +=1                                                             #왼쪽으로 돌아봐야 하니 +1
#     ni,nj = r,c
#     while True:
#         ni,nj = r+direction[d][0],c+direction[d][1]
#         if 0<=ni<M and 0<=nj<N and visited[ni][nj]==0 and arr[ni][nj] ==0 :#2-1번
#             rotate = 0
#             r,c = ni,nj
#             visited[r][c] = 1
#             result += 1
#             d = dir_change[d]
#             rotate +=1
#         elif 0<=ni<M and 0<=nj<N and arr[ni][nj]==1 and rotate <4:          #2-2 벽에막힐 경우
#             d = dir_change[d]
#             rotate += 1
#         elif 0<=ni<M and 0<=nj<N and visited[ni][nj]==1 and rotate <4:      #2-2 방문했을경우
#             d = dir_change[d]
#             rotate += 1
#         elif ni<0 or ni==M or nj<0 or nj ==N :                              #2-2 범위 밖일 경우
#             d = dir_change[d]
#             rotate += 1
#         elif rotate == 4 and 0<=r-direction[d][0]<M and 0<=c-direction[d][1]<N and arr[r-direction[d][0]][c-direction[d][1]] ==0:
#             r,c = r-direction[d][0],c-direction[d][1]
#             rotate = 0
#         elif rotate == 4 :
#             break
#     return

