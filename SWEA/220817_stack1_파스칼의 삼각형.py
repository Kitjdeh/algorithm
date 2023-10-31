import sys

sys.stdin = open('220817_stack1_파스칼의 삼각형.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print(f'#{tc}')
    arr = [1]                                   #시작 값 세팅
    for i in range(1,N+1):
        a = list([0] * i)                       #i번째 행렬에 들어가니 i개만큼만 생성
        arr.append(0)                           #제일 마지막 1을 1+0 =1 로 받을 0 생성
        for j in range(1,i):                    #i번째 행렬은 i-1번 계산이 일어남
            a[j] = arr[j]+arr[j-1]
        a[0] = 1                                #제일 마지막 1 변경
        arr =a
        print(f'{" ".join(map(str,arr))}')
