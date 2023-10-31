# 말처럼 K번 움직이고 나머지는 그냥 움직임
# bfs로 훑어야함
# 몇번 말처럼 움직이며 가는 지 체크해야함
# visited를 3차원으로 간다 [x][y][horse]
# 종료조건 [W-1][H-1]도착
# pop 값으로
# 1. 원숭이로 한칸 기어가기
# 2. 말로 호다닥 날아가기

from collections import deque
horse = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
monkey=[[1,0],[-1,0],[0,1],[0,-1]]

def bfs():
    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1
    while q:
        x,y,z = q.popleft()
        #[W-1,H-1]도착했으면 => 종료
        if x==H-1 and y ==W-1:
            for i in range(W):
                print(visited[i])
            return visited[x][y][z]-1
        for di,dj in monkey:
            ni,nj = x+di,y+dj
            # 원숭이로 갔는데 방문 안했다? -> 우선 방문
            if 0<=ni<H and 0<=nj<W and visited[ni][nj][z] == 0 and arr[ni][nj]==0:
                visited[ni][nj][z] = visited[x][y][z]+1
                q.append([ni,nj,z])
        #아직 말 사용을 다 안했으면 말 체크
        if z<K:
            for hi,hj in horse:
                ni,nj = x+hi,y+hj
                # 말타고 갈 수 있는곳이 정상 arr이며 0인 지점일 경우
                if 0<=ni<H and 0<=nj<W and arr[ni][nj]==0:
                    #빠꾸 방지를 위해 visited확인
                    if visited[ni][nj][z+1] == 0:
                        #말타고 간거니 z도 1칸 올려주시고
                        visited[ni][nj][z+1] = visited[x][y][z]+1
                        q.append([ni,nj,z+1])
    #while 끝났는데 종료 조건 안뜸? -> ㅈ망
    return -1

K = int(input())
W,H = map(int,input().split())
arr = [[0]*W for _ in range(H)]
for i in range(H):
    arr[i] = list(map(int,input().split()))
print(bfs())