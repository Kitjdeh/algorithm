def find_set(x):
    while x!=rep[x]:
        x = rep[x]
    return x

def union(x,y):
    rep[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    edge = []
    for i in range(0,2*M,2):
        edge.append([arr[i],arr[i+1]])
    edge.sort()
    rep = [i for i in range(N+1)]
    for a,b in edge:
        if find_set(a) != find_set(b):
            union(a,b)
    for i in range(1,N+1):
        rep[i] = find_set(i)
    cnt = 0
    head = []
    for i in range(1,N+1):
        if rep[i] not in head:
            head.append(rep[i])
            cnt +=1
    print(f'#{tc} {cnt}')