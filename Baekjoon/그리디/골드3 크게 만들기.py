from collections import deque
# num = deque(num)

N,K = map(int,input().split())
arr = list(map(int,input()))
stack=[]

#stack 생성
#1. N번의 for문에서 K개를 거른다
#2. 넣으려는 숫자가 뭔지 찾는 작업이 필요함
#3. 해당 자릿수에 대한 확인이 필요
#4-1. 배열의 i번쨰 숫자 num의 경우 stack에 넣기전에 stack 맨뒤 (stack[-1])보다 크다면 해당 스택을 지움
#4-2. K번만 하면 되니까 cnt 값을 -1씩 해서 0 되면 종료될 수 있게 and 조건으로 넣어줌

cnt = K
for num in arr:
    while stack and num > stack[-1] and cnt:
        stack.pop()
        cnt += -1
    stack.append(num)
stack = stack[:N-K]
print("".join(map(str,stack))