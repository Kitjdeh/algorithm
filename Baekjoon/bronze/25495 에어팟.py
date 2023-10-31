N = int(input())
arr = list(map(int,input().split()))
#이전 휴대폰과 다른 숫자면 소모량 t = 2
#이전 휴대폰과 같은 숫자면 소모량 t *= 2
#S에 각 소모량 값들을 더함
#시작은 무조건 소모량 2 이니 1~N-1까지 보면된다 (index0은 걍 2니까)
t =2
S =2
charging=[]
for i in range(1,N):
    if arr[i] == arr[i-1]:
        if t ==0:
            t =2
            S +=t
        else:
            t *=2
            S +=t
            if S>=100:
                S=0
                t=0
    else:
        t = 2
        S +=2
        if S>=100:
            S =0
            t = 0
print(S)


