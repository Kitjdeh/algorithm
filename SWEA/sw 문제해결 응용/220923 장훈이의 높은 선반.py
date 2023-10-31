import sys
sys.stdin = open("220923장훈이의높은 선반.txt")
# 점원들의 키를 조합하여 B보다 큰 값이 나오게 설정하여 result에 삽입

def f(s,i,A,B):                         #s: 지금까지의 총합, i 진행 횟수,A=arr,B=목표값
    global result
    if s >=B or i ==N:
        if B<=s<=result:                #전부 포함하지 않는 경우 거르기 위함
            result = s
        return
    else:
        f(s,i+1,A,B)                    #i 번째 포함하지 않는경우
        f(s+A[i],i+1,A,B)               #i 번째 포함하는 경우

T = int(input())
for tc in range(1,T+1):
    N,B = map(int,input().split())
    arr = list(map(int,input().split()))
    result = 0
    for i in range(N):
        result += arr[i]
    f(0,0,arr,B)
    print(f'#{tc} {result-B}')

