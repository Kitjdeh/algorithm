import sys
sys.stdin = open("백만장자 프로젝트.txt")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt =0
    max_v = 0

    for i in range(N-1,-1,-1):
        if max_v<arr[i]:
            max_v = arr[i]
        else:
            cnt += max_v-arr[i]
    print(f"#{tc} {cnt}")