N = int(input())
arr = [0]*N
for i in range(N):
    arr[i] = list(map(int,input().split()))
# arr.sort()
# #s1 < s2 면 무조건 arr[s1]<arr[s2]여야 중복이 안 일어난다
# #arr 0인덱스를 정렬한 후 1인덱스로 오름차순이 되도록 한다면 중복이 안일어난다
# t = 0
# cnt =0
# while True:
#     if t >= len(arr)-1:
#         break
#     elif arr[t][1] <arr[t+1][1]:
#         t +=1
#     else:
#         arr.pop(t+1)
#         cnt +=1
#
# print(cnt)
def cut(n,i):
