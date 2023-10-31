def enq(n):
    global last
    last +=1
    heap[last] = n
    c = last
    p = c //2
    while p and heap[p] >heap[c]:               #삽입 후 수정 조건: 부모가 있음 and 부모가 자식보다 큼
        heap[p],heap[c] = heap[c],heap[p]       #자식이 부모자리로 이동
        c = p                                   #자식 index 가 부모 index로
        p = c//2                                #부모 index 수정
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    last=0
    heap = [0] *(N+1)
    for i in range(N):
        enq(arr[i])
    result = 0
    c = N
    p = c//2
    while p:
        result +=heap[p]
        c = p
        p = c//2
    print(f'#{tc} {result}')