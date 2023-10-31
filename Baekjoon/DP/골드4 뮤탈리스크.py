#1. 9 / 3 / 1


N = int(input())
attack = [9,3,1]
arr = list(map(int,input().split()))
arr.sort(reverse=True)
cnt = 0
while True:
    for i in range(N):
        if arr[i]:
            arr[i] = arr[i] - attack[i]
            if arr[i] <0:
                arr[i] = 0
        else:
            break

    arr.sort(reverse=True)
    cnt += 1
    if arr[0] ==0:
        break

print(cnt)