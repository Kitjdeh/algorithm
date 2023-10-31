# 순서 상관 없이 전부 방문 해야 함, 최소 이동 횟수 구해야 함
#BFS
#1. 다음 턴에 갈 next 현재 체크할 now 구분
#2. now 턴에 not visited 에 -1이 아니면 next에 넣는다.
#2-1. point = 7 *[0] 중 i 있으면 point[i] =1
#3. now가 다 끝나면 cnt +1

#1~6은 한개씩 밖에 없음
#1~6을 방문하는 순서를 맞춰야 함
#6!갯수 확인?
#bfs에 시작점과 6! 중 한개의 순서인 num_order를 넣어준다.
#point에 순서가 맞게 입력이 된다면 거리를 체크한다.
def factorial(tmp):
    if len(tmp) == 6:
        numbers_order.append(tmp)
    else:
        for i in range(1,7):
            if i not in tmp:
                temp = tmp[:]
                temp.append(i)
                factorial(temp)
def BFS(r,c,num_order):
    now = [[r,c]]
    next = []
    point = [0]*6
    visited = [[0]*5 for _ in range(5)]
    cnt = 1
    num_cnt = 0
    while now:
        x,y = now.pop(0)
        for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni,nj = x+di,y+dj
            if ni<0 or ni>4 or nj<0 or nj>4 or visited[ni][nj]==1 or arr[ni][nj] == -1:
                continue
            else:
                visited[ni][nj] = 1
                next.append([ni,nj])
                num = arr[ni][nj]
                if num != -1 and num !=0:
                    if point[num_cnt] == num:
                        point[num] = 1
                        num_cnt +=1
                    else:
                        return
        if sum(point) == 6:
            break
        if not now and next:
            now = next[:]
            next = []
            cnt +=1
            # print(cnt,point)
    if sum(point) == 6:
        return cnt
    else:
        return -1
arr = [0]*5
for i in range(5):
    arr[i] = list(map(int,input().split()))
r,c = map(int,input().split())

numbers_order = []
factorial([])
for num_order in numbers_order:
    BFS(r,c,num_order)