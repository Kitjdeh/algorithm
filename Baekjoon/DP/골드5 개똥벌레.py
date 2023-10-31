#1. 총 N번의 숫자를 받는다 (석순-종유석-석순-종유석 ...)
#2. 선택한 구간은 정수가 아닌 정수와 정수 사
# 이를 지나간다 (ex 3과 4 사이를 지난다 -> 3도 아니고 4도 아닌 숫자
#3. 높이가 H이면 선택 할 수 있는 길은 5개이다
#(H=5 -> 0~1 / 1~2 / 2~3 / 3~4/ 4~5)
#4. 종유석,석순의 길이를 x2+1 하여 홀수는 지나가는 경로, 짝수는 종유석 길이로 설정한다.
#5. 한개를 받을때 마다 해당 길이를 +1 하여 다음 차수에 누적시킨다
# 4 , 5
# 1/ 3/ 4/ 2
# --------------
#----------천장10 (5x2)
# 0  1  1  2
# 0  1  1  2
# 0  1  2  3
# 0  1  2  3
# 0  1  2  2
# 0  1  1  1
# 0  0  1  1
# 1  1  2  2
# 1  1  2  2
#-----------바닥 0
# 처음 받을 때 높이가 5 라면 바닥 0과 천장 10 카운트 X=> 총 2*H-1개의 array 생성
# N,H = map(int,input().split())
# DP = [0]*(2*H-1)
#1
# for i in range(N):
#     #1-1
#     num = int(input())
#     if i % 2 ==0:
#         for j in range(2*num):
#             DP[j] +=1
#     else:
#         for j in range(2*num):
#             DP[(2*H-2)-j] +=1
# min_value = min(DP)
# cnt = 0
# for i in DP:
#     if i == min_value:
#         cnt +=1
# print(min_value,cnt)

# import sys
# import time
# start = time.time()
# input = sys.stdin.readline
#
# N,H = map(int,input().split())
#
# arr = [0]*N
# for i in range(N):
#     arr[i] = int(input())
# DP_bot = [0]*H
# DP_top = [0]*H
# for i in range(0,N,2):
#     for j in range(arr[i]):
#         DP_bot[j] +=1
# for i in range(1,N,2):
#     for j in range(arr[i]):
#         DP_top[j] += 1
#         # DP_top[H-j-1] += 1
#
# min_value = 100000000000
# cnt = 0
# for i in range(H):
#     if DP_bot[i]+DP_top[H-i-1] == min_value:
#         cnt +=1
#     elif DP_bot[i]+DP_top[H-i-1] <min_value:
#         cnt = 1
#         min_value = DP_bot[i]+DP_top[H-i-1]
# print(min_value,cnt)

# print("time :", time.time() - start)

import sys
import time
input = sys.stdin.readline
import time
start = time.time()

N,H = map(int,input().split())
arr = [0]*N
for i in range(N):
    arr[i] = int(input())
DP = [0]*H
for i in range(0,N,2):
    for j in range(arr[i]):
        DP[j] +=1
for i in range(1,N,2):
    for j in range(arr[i]):
        DP[H-j-1] += 1
min_value = DP[0]
cnt = 0
for i in DP:
    if i == min_value:
        cnt +=1
    elif i <min_value:
        cnt = 1
        min_value = i
print(min_value,cnt)
print("time :", time.time() - start)