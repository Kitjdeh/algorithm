#1. 제일 키 큰 거인을 때려야 함
#2. 센티보다 키가 큰 거인만 떄려야 함
#3. 10**5 만큼 길이의 리스트에 거인들의 키를 인덱스로 +1 씩한다.
#4. 맨 뒤에서 부터 n이 T가 될 때 가지 절반 씩 줄인다.
# N,H,T = map(int,input().split())
# # list_H = list(map(int,input().split()))
# arr = [0]*10**5
# T = int(input())
# for i in range(N):
#     p = int(input())
#     arr[p] +=1
# cnt = 0
# maxH = max(list_H)
# arr = [0]*(maxH+1)
# while cnt!=T and maxH >=H and maxH>1:
#     if arr[maxH] == 0:
#         maxH +=-1
#         pass
#     else:
#         arr[maxH] += -1
#         arr[maxH//2] +=1
#         cnt +=1
# if maxH>=H:
#     print("NO")
#     print(maxH)
# else:
#     print("YES")
#     print(cnt)

# 최대힙으로 계쏙 빼고 넣고 진행
# 망치수나 뚝배기 깰 거인이 남이있꺼나 키가 1일 경우
import heapq
heap = []
N,H,T = map(int,input().split())
for i in range(N):
    value = int(input())
    heapq.heappush(heap,-value)
cnt = 0
for i in range(T):
    temp = heapq.heappop(heap)
    maxH = -temp
    cnt +=1
    if maxH < H or maxH ==1:
        break
    else:
        temp = temp//2
        maxH = int(-temp)
        heapq.heappush(heap,temp)
if maxH < H:
    print("YES")
    print(cnt)
else:
    print("NO")
    print(maxH)
