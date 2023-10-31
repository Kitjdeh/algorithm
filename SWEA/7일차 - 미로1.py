import sys
sys.stdin = open('7일차 미로1.txt')
def f(i,j,s):
    global km
    visited = [[0] * 16 for i in range(16)]
    q=[]                                        #front/rear인 경우 : q=[0]*N*N,front=rear=-1
    km =[]
    q.append((i,j,s))                             #시작점 인큐 rear +=1, q[rear] = (i,j_
    visited[i][j] = 1                           #visited를 통하여 방문 여부를 확인하는 함수를 만든다.
    while q:                                    #front/rear인경우 --> front!=rear
        i,j,s = q.pop()                          #v <-디큐
        if maze[i][j] == 3:
            km.append(s)
            # return 1
        for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni,nj = i +di, j+dj
            if visited[ni][nj] ==0 and maze[ni][nj] !=1:
                q.append((ni,nj,s+1))
                visited[ni][nj] =1

    return 0


for tc in range(1,11):
    t = int(input())
    maze =[list(map(int,input())) for i in range(16)]
    print(f'#{tc} {f(1,1,0)}')
    tar = 100
    for i in range(len(km)):
        if km[i]<tar:
            tar = km[i]
    print(km)

#1 56
#2 48
#3 50
#4 0
#5 28
#6 64
#7 0
#8 44
#9 24
#10 48