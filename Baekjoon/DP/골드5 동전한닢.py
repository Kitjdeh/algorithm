# coin 값으로 x 가 들어온다
# y원을 만드는 방법은

# 1. (y-x) + x -> +1
# 2. (y-x-x) + x +x -> +1
# 3. (y-x-x-x) + x + x+ x -> +1
# ....
# 4. x + x+ x ... = y -> +1
# ex) 3원으로는 3,6,9,12... 원 을 1가지로 만들 수있음
# ->  4원이 추가된다면 -> 4원을 만드는 방법 +1 , 7원을 만드는 방법 (기존의 3원만드는법 +4) = 1가지 추가 , 11원을 만드는 방법 (기존의 7원 만드는 법 +4) = 1가지 추가

N,K = map(int,input().split())
DP = [0]*(K+1)
for i in range(N):
    coin= int(input())
    if coin <= K:
        DP[coin] +=1
        for j in range(coin,K+1):
            DP[j] += DP[j-coin]
print(DP[K])
