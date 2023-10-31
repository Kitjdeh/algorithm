# M,N = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# tomato=[]
# num = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] ==0:
#             tomato.append([i,j])
#             num +=1
# dir = [[-1,0],[1,0],[0,1],[0,-1]]
# cnt = 0
# while num:
#     L = len(tomato)
#     ch = 0
#     for i in range(L-1,-1,-1):
#         Tomato =tomato[i]
#         for di,dj in dir:
#             ni,nj = Tomato[0]+di,Tomato[1]+dj
#             if 0<=ni<N and 0<=nj<M and arr[ni][nj] ==1:
#                 arr[Tomato[0]][Tomato[1]] = 1
#                 tomato.pop(i)
#                 num += -1
#                 ch +=1
#                 break
#     cnt +=1
#     if ch ==0:
#         cnt = -1
#         break
# print(cnt)


M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
tomato=[]
num = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] ==1:
            tomato.append([i,j])
        elif arr[i][j] ==0:
            num +=1
dir = [[-1,0],[1,0],[0,1],[0,-1]]
cnt = 0
while num:
    # 다음 검사 할 토마토 리스트
    next_tomato =[]
    L = len(tomato)
    for i in range(L):
        Tomato =tomato[i]
        for di,dj in dir:
            ni,nj = Tomato[0]+di,Tomato[1]+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] ==0:
                arr[ni][nj] = 1
                next_tomato.append([ni,nj])
                num += -1
    # 기존 토마토 리스트는 다음번엔 확인할 필요 없으니 새로 추가한 애들로 바꿔줌
    tomato = next_tomato[0::]
    cnt +=1
    if L ==0:
        cnt = -1
        break
print(cnt)

