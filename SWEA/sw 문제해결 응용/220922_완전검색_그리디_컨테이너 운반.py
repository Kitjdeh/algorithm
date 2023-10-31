import sys
sys.stdin = open("220922_완전검색_그리디_컨테이너 운반.txt")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    container = list(map(int,input().split()))
    truck = list(map(int,input().split()))
    container.sort(reverse=True)                                    #컨테이너 중량 내림차순 정렬
    truck.sort(reverse=True)                                        #트럭 중량 내림차순 정렬

    cnt = 0
    stack = []
    result = 0
    for i in range(M):                                              #제일 중량 큰 트럭에서
        for j in range(len(container)):                             #큰 화물부터 넣어본다.
            if truck[i] >= container[j]:
                result += container[j]
                container.pop(j)
                break                                               #들어가지면 다음 트럭

    print(f'#{tc} {result}')
