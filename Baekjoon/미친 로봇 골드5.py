
# result =0
# luck = 0
# arr = [e,w,s,n]
# luck += e*w
# luck += w*e
# luck += s*n
# luck += n*s
# luck = 1-luck
# result = luck **(N-1)
# print(result)
#
#1. 동서남북으로 가면서 나올 수 있는 모든 경로를 체크한다.
#2. 확률을 계산한다..?
N, e, w, s, n = map(int,input().split())
e,w,s,n = e/100, w/100, s/100, n/100
direction = [[1,0],[-1,0],[0,-1],[0,1]]
lucky = [e,w,s,n]

visit = [[0]*(4*N) for i in range(4*N)]
cnt = 0
result  = 0
def dfs(cnt,x,y,visited,t):
    global N
    global result
    visited[x][y] = 1
    if cnt == N:
        result += t
        return
    else:
        for i in range(4):
            di,dj = direction[i][0],direction[i][1]
            ni,nj =x+di,y+dj
            if visited[ni][nj] ==0:
                dfs(cnt+1,ni,nj,visited,t*lucky[i])
                visited[ni][nj] = 0
dfs(cnt,2*N,2*N,visit,1)
print(result)