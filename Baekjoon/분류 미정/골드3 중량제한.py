# N개의 섬들중에서 두 개의 섬을 알려 주면 그 이동 경로들 중 다리들의 최솟값이 제일 큰 값을 찾아야함
#1. N,M 및 adj 관계로 데이터 수령
#1-1. A,B,C => adj[A]와 adj[B]에 각각 [B,C], [A,C] append
#1-2. 연결 해야할 두 섬 값 S,E 수령
#2. 모든 경로들의 최솟값들중 최댓값을 찾아야함 => BFS함수 필요
#3. BFS(현대 섬의 위치,현재 중량제한)
#3-1.종료조건 만약 섬의 위치가 E이면 종료
#3-2.
N,M = map(int,input().split())
adj = [[] for _ in range(N+1)]
S,E = map(int,input().split())
