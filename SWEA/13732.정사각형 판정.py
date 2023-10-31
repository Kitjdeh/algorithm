import sys
sys.stdin = open('13732정사각형판정.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr= [list(input()) for i in range(N)]
    cnt = 0
    sti = -1
    stj = -1
    k=0
    long=0
    result=0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "#":
                sti, stj = i, j
                break
        if stj != -1:
            break
    #arr에서 #가 연속하는 최댓값을 찾아서 정사각형의 길이 조건long으로 만든다
    for i in range(N):
        k = 0
        for j in range(N):
            if arr[i][j] == "#":
                k +=1
                cnt +=1
        if k>long :
            long = k
    #sti,stj에서 k만큼씩 i열,j열 #인지 확인
    if sti+long <=N and stj + long<=N:
        for i in range(sti,sti+long):
            for j in range(stj,stj+long):
                if arr[i][j] =="#":
                    result = "yes"
                else:
                    result = "no"
                    break
            if result =="no":
                break
    else:
        result = "no"
    #확인용: 전체 #의 수가 long*long인지 확인
    total = long*long
    if cnt != total:
        result = 'no'
    print(f"#{tc} {result}")



