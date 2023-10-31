#bfs 접근
#1. q 생성
#2. q의 p층에서 U와 D버튼으로 갈 수 있는 층 k를 확인
#3. k가 현재 visited가 0이라면 visited[k] = visited[p]+1
#4. q에 k append

F,S,G,U,D = map(int,input().split())
result = 0
visited = [0]*(F+1)
if G == S:
    print(0)
else:
    q = [S]
    visited[S] = 1
    cnt = 0
    while visited[G] ==0 and q:
        temp =[]
        cnt +=1
        for p in q:
            up,down = p+U,p-D
            if 0<up<=F and visited[up] ==0:
                visited[up] = cnt
                temp.append(up)
            if 0<down<=F and visited[down] ==0:
                visited[down] = cnt
                temp.append(down)
        q = temp[:]
    if visited[G]==0:
        print("use the stairs")
    else:
        print(visited[G])