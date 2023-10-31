def isprime(N):
    if N ==2:
        return 1
    elif N%2 ==0:
        return 0
    else:
        i = 2
        while 1*1<=N:
            if N%i ==0:
                return 0
            i +=1
        return 1
T = int(input())
for tc in range(1,T+1):
    a,b = map(int,input().split())
    s=0
    for i in range(a+1,b):
       s +=isprime(i) * i
    print(f'#{tc} {s}')