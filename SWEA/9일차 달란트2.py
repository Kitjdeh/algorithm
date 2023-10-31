import sys
sys.stdin=open('달란트2.txt')
T = int(input())
for tc in range(1,T+1):
    N, P = map(int,input().split())
    #숫자의 합이 일정 할 때 곱의 최댓값은 각 숫자들이 최대한 비슷한 경우이다.
    #N = P*k 인 경우 k 씩 분배
    #N = P*k +a 인경우 a개는 k+1 나머지는 k
    k = N//P
    a = N%P
    arr = [0]*P
    for i in range(P):
        arr[i] +=k
    for j in range(a):
        arr[j] +=1
    result =1
    for i in range(P):
        result *= arr[i]
    print(f"#{tc} {result}")