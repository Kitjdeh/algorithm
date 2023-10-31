#1명이 1명한테만 선행을 베품
#adj : dict로 정리
#visited: dict 생성
#N명을 len(N)의 리스트에 정리
answer = []
tc =0
while True:
    tc +=1
    N = int(input())
    if N == 0:
        break
    else:
        cnt = 0
        result = 0
        adj = {}
        visited = {}
        for i in range(N):
            p, q = input().split()
            adj[p] = q
            visited[p] = 0
        for p in adj:
            if visited[p]:
                pass
            else:
                while not visited[p]:
                    visited[p] = 1
                    p = adj[p]
                result += 1
    print(tc,result)