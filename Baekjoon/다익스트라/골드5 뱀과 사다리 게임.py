def bfs(n,c):
    global result

    return
N,M = map(int,input().split())
a = [[]]
arr = [[] for i in range(102)]
for _ in range(N+M):
    a,b = map(int,input().split())
    arr[a].append(b)
visited = [0]*101
visited[1] = 1
result = 0
bfs(1,0)
print(result)
stack = [1]
cnt  = 0
while visited[100] ==0:
    cnt = 1
    L = len(stack)
    for i in L:
        if arr[stack[i]] >0 and stack[i] > arr[stack[i]]:
            stack.pop(i)
            stack.append()
