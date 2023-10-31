T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    heap = [0] *(N+1)
    for _ in range(M):
        c,b = map(int,input().split())
        heap[c] = b
        p = c//2
        while p:
            heap[p] +=b
            c = p
            p = c//2
    print(f'#{tc} {heap[L]}')