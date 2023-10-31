T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    visited = [0]*1000001
    visited[N]= 1
    queue = [N]
    cnt = 0
    while visited[M] ==0:
        cnt +=1
        L = len(queue)              #pop를 L번 하면 된다.
        for i in range(L):
            a = queue.pop(0)
            A = [a+1,a-1,a*2,a-10]  #연산
            for j in A:
                if j == M:
                    visited[j] =cnt
                    break
                elif 0<j<1000001 and visited[j] == 0:#방문 안한 경우 이번이 제일 빠르니 cnt추가
                    visited[j] =cnt
                    queue.append(j)
    print(f'#{tc} {cnt}')
