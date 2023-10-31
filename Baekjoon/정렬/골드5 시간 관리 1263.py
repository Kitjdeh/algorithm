# 1. 소요시간, 마감 시간 중 마감시간을 기준으로 내림차순 정렬
# 2. 제일 늦은 시간 부터 마감 처리
# 3. 계속 진행하다 제일 먼저 처리해야 할 일 어칠

N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
    p,q = map(int,input().split())
    arr[i] = [p,q]
arr.sort(key = lambda x: x[1],reverse=True)
cnt = arr[0][1]
while arr:
    p,q = arr.pop(0)
    if cnt < q:
        q = cnt
    cnt = q-p
if cnt <0:
    print(-1)
else:
    print(cnt)
# 4
# 3 4
# 1 4
# 5 17
# 2 20
# ans: 0