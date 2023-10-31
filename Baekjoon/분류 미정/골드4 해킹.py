#  n / d / c로 처음 해킹 당한 컴퓨터 c가 주어진다
#  -> c부터 시작해서 나머지 컴퓨터 까지 도달하는데 걸리는 시간들 확인해서 max를 뽑는다.

#1. 감염된 a에서 시작해서 b감염 보다 a - c- b 가 더 빠르면 바꿔야 함 -> 다익스트라
#2. n * n 의 2차원 배열 을  생성 arr[p][q] = p에서 q까지 가는 최단 거리
#3. 우선 INF 박아 둔다.
#4. d갯 숫자만큼을 arr값들을 생성
#5. c에서 k 까지의 시간을 체크하는 Distance[k]를 생성한다.
#6. 방문을 확인하는 visited 생성
#7. 초기 Distance[k] = INF or (c와 맞닿아 있으면 c)
#8. Distance[k] = min(Distance[k],d[w]+arr[w][k])

tc = int(input())
for t in range(tc):
    print(1)
    n,d,c = map(int,input().split())
    INF = 10000000000000000000000000
    arr = [[INF]*(n+1) for _ in range(n+1)]
    visited = [0] *(n+1)
    for i in range(d):
        a,b,s = map(int,input().split())
        arr[b][a] = s
    Distance = [0]*n
    for i in range(n):
        Distance[i] = arr[c][i]
    #c를 제외한 나머지들을 거칠 경우의 거리들을 재확인 해야함
    visited[c] = 1
    for _ in range(d):
        if d ==c :
            pass
        else:
            # 일단 c에서 시작
            check_point = c
            #전체를 훑으면서 INF아닌지랑 방문 여부 확인
            for i in range(n+1):
                #방문 여부 + 지금 j까지의 거리가 제일 짧은애 하나 뽑기
                if visited[n] == 0 and Distance[i]<Distance[check_point]:
                    check_point = i
            visited[check_point] = 1
            #지금 젤 짧은애하나 뽑아서 얘를 통해서 가른 다른 루트들 변동 확인
            for i in range(n+1):
                if visited[i] == 0 and arr[check_point][i] < INF:
                    Distance[i] = min(Distance[i],Distance[check_point]+arr[check_point][i])



