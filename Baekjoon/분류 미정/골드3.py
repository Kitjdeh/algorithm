def dfs(x,y,direct,cnt):
    global W
    global H
    if 0<=x<H and 0<=y<W and arr[x][y] == 'C':
        result.append(cnt)
        return
    else:
        visited[x][y] = 1
        for di, dj in direction:
            ni,nj = x+di,y+dj
            print(ni,nj)
            if 0<=ni<H and 0<=nj<W and visited[ni][nj] ==0 and arr[ni][nj] != '*':
                if [di,dj] == direct:
                    print(di,dj)
                    dfs(ni,nj,[di,dj],cnt)
                else:
                    new_dir = [di,dj]
                    dfs(ni,nj,new_dir,cnt+1)
        visited[x][y] = 0
W ,H = map(int,input().split())
arr= [list(input()) for _ in range(H)]
print(arr)
direction=[[1,0],[0,1],[-1,0],[0,-1]]
visited = [[0] * H for _ in range(W)]
result=[]
SE =[]
for i in range(W):
    for j in range(H):
        if arr[j][i] == 'C':
            SE.append([i,j])
s1,s2 = SE[0][0],SE[0][1]
arr[s1][s2] = '.'
for a,b in direction:
    dfs(s1,s2,[s1,s2],0)
print(result)

