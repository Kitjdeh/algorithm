import sys
sys.stdin = open('220930요리사.txt')
def comb(A,N,r):
    result =[]
    if r ==1:
        for i in A:
            result.append([i])
    elif r>1:
        for i in range(N-r+1):
            for j in comb(A[i+1::],N,r-1):
                result.append([A[i]]+j)
    return result

def f(A,N,r):
    if r == N//2:
        return

def taste(A,B):
    S = 0
    L = len(A)
    for i in A:
        for j in A:
            S+= arr[i-1][j-1]
    for i in B:
        for j in B:
            S+= -arr[i-1][j-1]
    return S
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    minV = 1000000000
    arr = [list(map(int,input().split())) for _ in range(N)]
    food_list = [i for i in range(1,N+1)]
    B=[]
    r = N//2
    result = comb(food_list,N,r)
    for A in result:
        B = list(set(food_list)-set(A))
        # for j in food_list:
        #     if j not in A:
        #         B.append(j)
        valence = abs(taste(A,B))
        if minV>valence:
            minV = valence
    print(f'#{tc} {minV}')

