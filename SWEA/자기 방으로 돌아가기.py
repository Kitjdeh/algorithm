import sys
sys.stdin = open('자기방으로 돌아가기.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [0] *200
    for i in range(N):
        p,q = list(map(int,input().split()))
        a = p - 1
        b = q - 1
        if a<b:
            for j in range(a//2,b//2+1):
                arr[j] +=1
        else:
            for j in range(b//2,a//2+1):
                arr[j] +=1

    max_move = 0
    for i in range(200):
        if arr[i]>max_move:
            max_move = arr[i]
    print(f"#{tc} {max_move}")