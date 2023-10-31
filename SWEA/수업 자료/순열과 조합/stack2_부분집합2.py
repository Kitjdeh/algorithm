def f(i,N,s,t):         #i-1원소까지의 합 s
    global answer
    global cnt
    cnt+=1
    if i ==N:        #모든 원소가 고려된 경우
        if s ==t: #부분집합이 t면
            answer +=1
        return
    elif s>t:
        return
    else:
        f(i+1,N,s+A[i],t)   #A[i]가 포함된 경우
        f(i+1,N,s,t)        #A[i]가 포함되지 않은 경우
    # if s==t:            #부분집합의 합이 t면
    #     answer +=1
A =[1,2,3,4,5]
bit = [0]*5
answer = 0
s = 0
cnt = 0
f(0,5,0,10)
print(answer, cnt)