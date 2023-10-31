#4개의 톱니바퀴 각 상태는 N(==0)이나 S(==1)의 상태
#바뀐다 or 안바뀐다 => 회전 => rotation 필요
#deque는 이럴 때 쓰는 것이다
#def rotation(회전 시키는 톱니바퀴의 번호, 회전 방향)
#1번이 돌경우 => 2번 회전 여부 -> 3 -> 4
#2번 - > 1번 회전여부 -> 2번회전여부 ->4 회전여부
#3번 -> 4 번회전여부 - >2번 회전여부 -> 1번 회전여부
#4번 -> 3번 회전여부 -> 2 -> 1 회전여부

#체크 다한 후에 deque로 한번에 돌린다.
#시계방향 회전 -> 오른쪽 회전 -> (1)
#반시계방향 회전 -> 왼쪽 회전 -> (-1)

# from collections import deque
# def rotation(k,d):
#     cycle =[0]*4
#     if k==1:
#         cycle[0] = d
#         if arr[0][2] != arr[1][6]:
#             cycle[1] = -d
#             if arr[1][2] != arr[2][6]:
#                 cycle[2] = d
#                 if arr[2][2] != arr[3][6]:
#                     cycle[3] = -d
#     elif k==2:
#         cycle[1] = d
#         if arr[1][6] != arr[0][2]:
#             cycle[0] = -d
#         if arr[1][2] != arr[2][6]:
#             cycle[2] = -d
#             if arr[2][2] !=arr[3][6]:
#                 cycle[3] = d
#     elif k==3:
#         cycle[2]=d
#         if arr[2][2] != arr[3][6]:
#             cycle[3] = -d
#         if arr[2][6] != arr[1][2]:
#             cycle[1] = -d
#             if arr[0][2] != arr[1][6]:
#                 cycle[0] = d
#     elif k==4:
#         cycle[3] = d
#         if arr[2][2] !=arr[3][6]:
#             cycle[2] = -d
#             if arr[2][6] != arr[1][2]:
#                 cycle[1] = d
#                 if arr[0][2] != arr[1][6]:
#                     cycle[0] = -d
#     for i in range(4):
#         if cycle[i]:
#             a = arr[i]
#             a = deque(a)
#             a.rotate(cycle[i])
#             arr[i] = list(a)
#     return
# arr = [0]*4
# for i in range(4):
#     arr[i] = list(map(int,list(input())))
# K = int(input())
# cnt = 0
# for i in range(K):
#     num,direction = map(int,input().split())
#     rotation(num,direction)
# for i in range(4):
#     if arr[i][0] == 1:
#         cnt += 2**i
# print(cnt)


# test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# test = deque(test)
# test.rotate(2)
# result = list(test)
# result
# [8, 9, 1, 2, 3, 4, 5, 6, 7]
# 11111110
# 00000000
# 11111111
# 11111111
# 1
# 2 -1