N =int(input())
arr = [int(input()) for _ in range(N)]
cnt = 0
k=1
while len(arr) != 1: #1번만 남을떄까지
    if arr[0] ==max(arr):
        if arr[1] != arr[0]:
            arr.pop(1)
        else:
            arr[0] +=1
            arr[1] +=-1
            cnt +=1
    else:
        if 0<k<len(arr)-1:  #2번~끝번까지 매수차례확인
            k +=1           #다음 매수차례
        else:
            k=1             #끝번이면 다시 1부터
        if arr[k] <arr[0]:  #1번보다 낮으면 pop
            arr.pop(k)
        elif arr[k] ==max(arr):#최댓값이면 줄이고 본인 up
            arr[0] +=1
            arr[k] += -1
            cnt +=1          #매수한거니 +1

print(cnt)
# T = int(input())
# num = [T]
# for _ in range(N-1):
#     K = int(input())
#     if T >= K:
#         num.append(K)
# arr = [[0]*i for i in num]
#
#
#
#
#
# arr=[[0]*int(input()) for i in range(N)]
# print(arr)
#
