# 제일 적은 값을 3으로 나눔
# 나머지 가 0 이면 pass
# 1이면 남는 2를 다음 숫자에 누적
# (만약 다음 숫자가 1이면? -> tmp에 보관)
#
N = int(input())
arr = list(map(int,input().split()))
# arr.sort()
cnt = 0
total = sum(arr)
if total%3 !=0:
    print("NO")
else:
    for i in arr:
        p = i//2
        cnt += p
    if cnt >= total//3:
        print("YES")
    else:
        print("NO")