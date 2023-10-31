# a,b 숫자가 c= a+b를 계산 후 c,c로 바뀐다
#만들 수 있는 가장 작은 점수를 계산 -> 가장 작은 수 끼리 더한다.
# 오름 차순을 유지 하며 더한다.
# 우선 순위 큐로 값들을 넣는다.
# 제일 작은 값을 pop로 2번 뺀다.
# 2번 뺀 a,b를 더한 c 를 생성
# c를 2번 넣는다.

from heapq import heappush
from heapq import heappop
import heapq
import sys
heap = []
n, m = map(int,sys.stdin.readline().rstrip("\n").split())
arr = list(map(int,sys.stdin.readline().rstrip("\n").split()))
# arr.sort()
for i in arr:
    heapq.heappush(heap,i)
for i in range(m):
    p = heapq.heappop(heap)
    q = heapq.heappop(heap)
    r = p+q
    heapq.heappush(heap,r)
    heapq.heappush(heap,r)
print(sum(heap))
