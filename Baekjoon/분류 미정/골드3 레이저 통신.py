#1. C점 2개를 찾아서 S,E로 설정
#2. S점 기준으로 거울이 없이 가는 곳들을 0으로 설정
#3. 0으로 설정된 곳들을 next 리스트에 넣는다.
#4. next 값들을 for문
#4-1. next[i] 기준으로 좌우 H, 상하 W만큼 돌린다.
#4-2. 벽(*)이면 종료 , . 이면 계속
#4-3. 기존 값보다 작으면 교체, 크면 무시
#4-4. next 다쓰면 다음 next로 다음 함수
def maze():
    next = []


W,H = map(int,input().split())
arr = [[0]*W for _ in range(H)]
for i in range(H):
    arr[i] = list((input()))
C = []
direction = [[1,0],[0,1],[-1,0],[0,-1]]
mirror = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if arr[i][j] == 'C':
            C.append([i,j])
S = C[0]
E = C[1]
now = [S]

cnt = 0
while mirror[E[0]][E[1]] ==0:
    next=[]
    for w,v in now:
        for di,dj in direction:
            k = 1
            while True:
                ni,nj = w+di*k,v+dj*k
                if 0<=ni<H and 0<=nj<W and arr[ni][nj] != '*' and mirror[ni][nj] ==0:
                    mirror[ni][nj] = cnt
                    next.append([ni,nj])
                elif 0<=ni<H and 0<=nj<W and arr[ni][nj] != '*' and mirror[ni][nj] >cnt:
                    mirror[ni][nj] = cnt
                    next.append([ni,nj])
                else:
                    break
                k +=1
    cnt +=1
    now = next[:]
# print(S)
# for i in range(H):
#     print(mirror[i])
print(mirror[E[0]][E[1]])
