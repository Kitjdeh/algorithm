import sys
sys.stdin = open('암호생성기.txt')
for tc in range(10):
    t= int(input())
    arr = list(map(int,input().split()))
    k = 1
    while arr[-1] >0:                   #끝자리 크기가 종료 여부
        c = arr.pop(0)
        c += -k
        arr.append(c)
        k +=1
        if k>5:
            k = 1
    arr[-1] = 0                         #음수일 경우 방지
    arr = map(str,arr)
    print(f'#{t} {" ".join(arr)}')