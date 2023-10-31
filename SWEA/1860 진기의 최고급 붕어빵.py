import sys
sys.stdin = open('1860 진기의 최고급 붕어빵.txt')
T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    #붕어빵을 만들어 두는곳을 stack
    #M초 후 붕어빵 k개를 stack에 append
    #그동안 손님들이 오면 불가능
    #시간을 확인하는 t
    #붕어빵손님 도착 리스트 arr
    #stack 에 0을 넣고 시작하여 1초 단위로 돌아가는 while 문 생성
    #1초 가 끝났을때 len(stack)이 0이면 impossible
    stack=[]
    arr=list(map(int,input().split()))
    arr.sort()
    t = 0
    result = "Possible"
    while len(stack)<N:
        if (t % M ==0) and t !=0:
            for _ in range(K):
                stack.append(1)
        for i in arr:
            if t == i:
                if len(stack) ==0:
                    result = "Impossible"
                    break
                else:
                    stack.pop()

        if result == "Impossible":
            break
        t +=1
    print(f"#{tc} {result}")

