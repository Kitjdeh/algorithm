import sys
sys.stdin = open('Dijkstra - 5250최소비용 문제.txt')

def enq(n):
    global last
    last += 1  # 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 key 추가

    c = last
    p = c // 2  # 완전이진트리에서 부모 정점 번호
    while p and D[heap[p][0]][heap[p][1]] > D[heap[c][0]][heap[c][1]]:  # 부모가 있고, 부모 > 자식 인경우 자리 교환
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


def deq():
    global last
    tmp = heap[1]  # 루트 백업
    heap[1] = heap[last]  # 삭제할 노드의 키를 루트에 복사
    last -= 1  # 마지막 노드 삭제
    p = 1  # 루트에 옮긴 값을 자식과 비교
    c = p * 2  # 왼쪽 자식
    while c <= last:  # 자식이 하나라도 있으면
        if c + 1 <= last and D[heap[c][0]][heap[c][1]] > D[heap[c + 1][0]][heap[c + 1][1]]:  # 오른쪽 자식도 있고, 오른쪽 자식이 더 작으면
            c += 1  # 비교 대상을 오른쪽 자식으로 정함
        if D[heap[p][0]][heap[p][1]] > D[heap[c][0]][heap[c][1]]:  # 자식이 더 작으면 최소힙 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c  # 자식을 새로운 부모로
            c = p * 2  # 왼쪽 자식 번호를 계산
        else:  # 부모가 더 작으면
            break  # 비교 중단,
    return tmp


def dijkstra(N):
    U = [[0] * N for _ in range(N)]
    D[0][0] = 0
    enq((0, 0))
    while last:  # 출발점 뺀 N*N-1개의 정점에 대한 비용 결정
        wi, wj = deq()
        if U[wi][wj] == 0:
            U[wi][wj] = 1  # 현재 D[w]가 최소인 w는 비용 결정
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # w와 인접인 v에 대해 비용 갱신
                vi, vj = wi + di, wj + dj
                if 0 <= vi < N and 0 <= vj < N and U[vi][vj] == 0:
                    diff = 1
                    if arr[vi][vj] > arr[wi][wj]:
                        diff += arr[vi][vj] - arr[wi][wj]
                    if D[vi][vj] > D[wi][wj] + diff:
                        D[vi][vj] = D[wi][wj] + diff
                    enq((vi, vj))

    return D[N - 1][N - 1]


INF = 1000000000
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    heap = [0] * (N * N)
    D = [[INF] * N for _ in range(N)]
    last = 0
    print(f'#{tc} {dijkstra(N)}')