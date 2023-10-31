#1. 1~N번 까지의 덩치 등수는 중복일 수도 아닐 수도 있따.
#2. 그럼 각각 따로 체크를 해야함

N = int(input())
arr = [0]*N
for i in range(N):
    arr[i] = list(map(int,input().split()))
result = ''
STR = ''
for i in range(N):
    rank = 1
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank +=1

    result += str(rank)
    result += ' '
print(result)