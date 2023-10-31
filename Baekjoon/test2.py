# 문제 1
from collections import deque
f,s,g,u,d = map(int, input().split())
#f: 총 층수 s: 지금 있는 곳, g:도착할 층, u:위로 올라 갈 수 있는 층 d:아래로 내려갈 수 있는 층 수
visited = [True]+[False]*f
print(visited)
# print(visited)
ans = 0
def bfs(start, end, n):
    global ans
    visited[start] = True
    queue = deque([start,n])
    while(queue):
        x = queue.popleft()
        n = queue.popleft()
        visited[x] = True
        # print(x,n)
        if x == end:
            ans = n
            break
        y = x+u
        z = x-d
        if f >= y:
            if not visited[y]:
                queue.append(y)
                queue.append(n+1)
        if 0 < z:
            if not visited[z]:
                queue.append(z)
                queue.append(n+1)
        # print(queue)
if s==g:
    print(0)
else:
    bfs(s,g,0)
    if ans ==0:
        print("use the stairs")
    else:
        print(ans)