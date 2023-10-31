import sys
sys.setrecursionlimit(10**6)
def f(x,y,i,cnt):
    global N
    global M
    global minV
    if x ==N and y ==M:
        if minV > cnt:
            minV = cnt
        return minV
    elif cnt >minV:
        return
    else:
        for di,dj in direction:
            ni,nj = x+di,y+dj
            if 0<=ni<=N and 0<=nj<=M and visited[ni][nj] ==0 and arr[ni][nj] ==0:
                visited[ni][nj] = 1
                f(ni,nj,i,cnt+1)
                visited[ni][nj] = 0
            elif 0<=ni<N and 0<=nj<M and arr[ni][nj] ==1 and i ==0:
                visited[ni][nj] = 1
                f(ni,nj,i+1,cnt+1)
                visited[ni][nj] = 0
    return

N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
N,M =N-1,M-1
direction = [[1,0],[-1,0],[0,1],[0,-1]]
minV = 1000000000000
f(0,0,0,1)
if minV ==1000000000000:
    print(-1)
else:
    print(minV)