#노드 하나 방문마다 해당 부모들 올라가면서 visited 체크
#0이 될때 까지 visited 없으면 0 아니면 막힌 부분 print
import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
visited = set()
node = [0]*Q
for i in range(Q):
    t = int(input())
    node.append(t)
    result = 0
    temp = t
    while temp > 1:
        if temp in visited:
            result = temp
        temp = temp//2
    visited.add(t)
    print(result)