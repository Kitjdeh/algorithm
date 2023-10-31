# def f(i,N,s,t):         #i-1원소까지의 합 s
#     global answer
#     global cnt
#     cnt+=1
#     if i ==N:        #모든 원소가 고려된 경우
#         if s ==t: #부분집합이 t면
#             answer +=1
#         return
#     elif s>t:
#         return
#     else:
#         f(i+1,N,s+A[i],t)   #A[i]가 포함된 경우
#         f(i+1,N,s,t)        #A[i]가 포함되지 않은 경우
#     # if s==t:            #부분집합의 합이 t면
#     #     answer +=1
# 길이 N의 arr에서 r개의 원소를 가지는 부분집합

def f(i,N,arr,r):
    result=[]
    # 재귀로 N번 진행하면(=넣거나 안넣거나 를 N번) i가 N이 됨
    if i ==N:
        for i in range(N):
            if bit[i] ==1:           #1은 넣은 경우
                result.append(arr[i])
        if len(result) == r:        #원하는 갯수
            ord.append(result)
        return
    else:
        candidate = [0,1]
        for x in candidate:         # 1 이나 0 둘중 한개를 x가 가짐
            bit[i] = x              # 1인 경우 0인 경우 2가지로 자동 재귀 적용
            f(i+1,N,arr,r)
            bit[i]=0                #다시 써야 하니 0으로 복구
A =[1,2,3,4,5]
N = len(A)
bit = [0]*N
result =[]
ord =[]
f(0,N,A,2)
print(ord)
print(len(ord))
# print(answer, cnt)
answer = 0
s = 0
cnt = 0