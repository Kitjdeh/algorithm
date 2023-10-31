def f(i,N):
    global answer
    if i == N:
        s = 0
        for i in range(N):
            if bit[i]==1:
                s +=A[i]
            if s == 10:
                answer +=1
    else:
        candidate = [0,1]
        for x in candidate:
            bit[i] = x
            f(i+1,N)
            bit[i] = 0
        # bit[i] = 1 # A[i]가 부분집합에 포함
        # f(i+1,N)
        # bit[i] = 0
        # f(i+1,N)

A =[1,2,3]
bit = [0]*3
answer = []
s = 0
f(0,3)
print(answer)
print(s)