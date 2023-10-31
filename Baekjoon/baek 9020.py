def prime(N):
    k = 2
    count = 0
    while k*k<= N:
        if N % k == 0:
            k +=1
            count +=1
            break
        else:
            k +=1
    if count == 0:
        return 0
    else:
        return 1
T = int(input())
for tc in range(T):
    A = int(input())
    N = int(A/2)
    #N은 짝수이고 N 이하인 소수 k가 골드바흐면 자동으로 N-k도 확인하게 되니 절반만 보면 된다.
    p, q = 0, 0
    for k in range(2,N+1):
        if (prime(k) == 0)and(prime(A-k)==0):
            p = k
            q = int(A-k)
    print(p,q)
