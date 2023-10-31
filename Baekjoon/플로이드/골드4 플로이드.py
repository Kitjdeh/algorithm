# I. data 수령
# I-1. a,b,c로 수령하는데 기존에 값이 있을 경우는 작은 숫자를 넣는다.
#II. N개의 도시에 대한 for 문
#II-1. 전체 arr 에서 i가 없는 루트들 확인
#II-2. i번 도시를 거쳐 x에서 y로 가는 비용 <-> 기존의 x에서 y로 가는 비용
# => arr[x][y]  arr[x][i] + arr[i][y]
#III. INF로 남은 경로가 있으면 확인하여 0으로 처리

# I. data 수령
N = int(input())
M = int(input())
INF = 1000000000
arr = [[INF]*(N+1) for _ in range(N+1)]
# I-1. a,b,c로 수령하는데 기존에 값이 있을 경우는 작은 숫자를 넣는다.

for _ in range(M):
    a,b,c = map(int,input().split())
    arr[a][b] = min(arr[a][b],c)
for i in range(N+1):
    arr[i][i] = 0

#II. N개의 도시에 대한 for 문
for i in range(1,N+1):
    for x in range(1,N+1):
        for y in range(1,N+1):
            # II-1. 전체 arr 에서 i가 없는 루트들 확인
            if x != i and y != i and arr[x][i] != INF and arr[i][y] !=INF and arr[x][y] > arr[x][i]+arr[i][y]:
                # II-2. i번 도시를 거쳐 x에서 y로 가는 비용 <-> 기존의 x에서 y로 가는 비용
                arr[x][y] = arr[x][i] + arr[i][y]

# III. INF로 남은 경로가 있으면 확인하여 0으로 처리
for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == INF:
            arr[i][j] = 0
for i in range(1,N+1):
    print(" ".join(map(str,arr[i][1:])))