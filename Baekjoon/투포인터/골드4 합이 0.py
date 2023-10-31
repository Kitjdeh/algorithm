# # N 명중 3명을 고르고 합이 0 이되는 경우
# # nCr?
# # 재귀 f(team,0,c)
# #1. n개 중 i번 점수를 를 team에 넣는다.
# #2. i를 넣은 후 f(team,i)
# #3. i+1~n 중 j를 team 에 넣고 f(team,j)
# # j+1~n 중 t를 넣고 합이 0이면 result +1
#
# def f(team,x,n):
#     global result
#     global N
#     if n == 3:
#         # print(team)
#         if sum(team) == 0:
#             result +=1
#         return
#     else:
#         for i in range(x,N):
#             tmp = team[:]
#             tmp.append(arr[i])
#             f(tmp,i+1,n+1)
#             # print(tmp)
#
# N = int(input())
# arr = list(map(int,input().split()))
# result = 0
# f([],0,0)
# print(result)

#1. 전체 arr를 정렬
#2. 0~N-2 중 i 번째 수 K를 뽑는다.
#3. i+1~N 중 투포인터로 합이 -K를 찾는다.

N = int(input())
arr = list(map(int,input().split()))
result = 0
arr.sort()

for i in range(N-2):
    K = arr[i]
    left,right = i+1,N-1
    max_idx = N
    while left < right:
        tmp = arr[left]+arr[right]
        if K+tmp == 0:
            if arr[left] == arr[right]:
                result += right - left
            else:
                if max_idx > right:
                    max_idx = right
                    while arr[max_idx] == arr[right]:
                        max_idx += -1
                result += right - max_idx
            left +=1
        elif K+tmp > 0:
            right += -1
        else:
            left +=1
print(result)