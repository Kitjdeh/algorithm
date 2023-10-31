# 빈 리스트 를 생성
# 1번 포트를 result에 담음
# for문을 돌려서 arr[i]값과 result[-1]을 비교함
# ex) 2 5 3 4 1
# result =[2]
# result[-1]=2
# arr[1] = 5
# 1.arr 값이 더 큼 => 안곂침
# append => result = [2,5]
# result = [2,5]
# arr[i] = 3
# 2.arr 값이 더 작음 => 곂침
# arr[i] (=3) 가 들어갈 자리 확인
# 5보다 작고 2보다 크니 5자리
# 5로 결정
# [2, 3]
# [2, 3, 4]
# [1, 3, 4]

# def biseacrch(start,end,target):
#     while start < end:
#         mid = (start+end)//2
#         if result[mid] < target:
#             start = mid +1
#         else:
#             end = mid
#
#     return end
#
# N = int(input())
# arr = list(map(int,input().split()))
# # arr = [0]+arr
# result = [arr[0]]
# cnt = 1
# for i in range(1,N):
#     if arr[i] <= result[-1]:
#         temp = biseacrch(0,len(result)-1,arr[i])
#         result[temp] = arr[i]
#     else:
#         result.append(arr[i])
# print(result)
# print(len(result))


n = int(input())

arr = [0] + list(map(int, input().split()))
ans = [0 for _ in range(n+1)]

for i in range(1, n+1):
    not_include = ans[i-1]
    include = 1
    for j in range(i-1, 0, -1):
        if arr[j] != -1 and arr[j] < arr[i]:
            include = 1 + ans[j]
            break
    if not_include > include:
        ans[i] = not_include
        arr[i] = -1
    else:
        ans[i] = include
    # print(ans,arr,i)
print(ans[n])
# ans arr i
# [0, 1, 0, 0, 0, 0, 0, 0] [0, 1, 5, 6, 2, 3, 4, 7] 1
# [0, 1, 2, 0, 0, 0, 0, 0] [0, 1, 5, 6, 2, 3, 4, 7] 2
# [0, 1, 2, 3, 0, 0, 0, 0] [0, 1, 5, 6, 2, 3, 4, 7] 3
# [0, 1, 2, 3, 3, 0, 0, 0] [0, 1, 5, 6, -1, 3, 4, 7] 4
# [0, 1, 2, 3, 3, 3, 0, 0] [0, 1, 5, 6, -1, -1, 4, 7] 5
# [0, 1, 2, 3, 3, 3, 3, 0] [0, 1, 5, 6, -1, -1, -1, 7] 6
# [0, 1, 2, 3, 3, 3, 3, 4] [0, 1, 5, 6, -1, -1, -1, 7] 7
# 4