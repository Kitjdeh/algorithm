import sys

sys.stdin = open('swea4861.txt')

T=int(input())
for tc in range(1,T+1):
    arr =[]
    N,M = map(int,input().split())
    for i in range(N):
        arr.append(list(input()))
    #가로,세로 2번 확인해야함
    #확인법: 가로 i번,과 -(m+i-n)확인
    #가로
    result = ''
    for i in range(N):
        for j in range(N-M+1):
            ch = arr[i][j:j+M]
            if ch == ch[::-1]:
                result =ch
                break
    #세로열 확인은 리스트로 한번에 확인이 여러우니 가로세로 반전을 준 후 가로와 동일하게
    all = []
    for i in range(N):
        re = []
        for j in range(N):
            re.append(arr[j][i])
        all.append(re)
    for i in range(N):
        for j in range(N-M+1):
            ch = all[i][j:j+M]
            if ch == ch[::-1]:
                result =ch
    print(f'#{tc} {"".join(result)}')