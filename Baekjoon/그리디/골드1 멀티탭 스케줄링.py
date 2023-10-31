#k번째 전기용품n을 사용하려 할 때 함수 MultiTap(n,k)
#stack=[]에 append하여 len값이 N이 될때 까지 진행하여 중복된 값이 없는 stack을 만든다.
#I. 기존의 멀티탭에 해당 용품이 있을 경우
#I-1. 종료
#II. 기존의 멀티탭에 해당 용품이 없을 경우
#II-1. 기존의 멀티탭에서 다시 쓰지 않을 것으로 바꿔야함
#II-2. k번째부터 총 K까지 돌면서 이미 나온 것들은 value에 append한다.
#II-3. 순회가 끝났을 경우 len(value)가 N보다 작다면 not in value를 찾아서 교환한다
#II-4. 순회가 끝났을 경우 len(value)==N이면 value 맨뒤에 있는 값의 stack.index로 찾아 바꾼다.

def MultiTap(n,k):
    global cnt
    # I. 기존의 멀티탭에 해당 용품이 있을 경우
    if n in stack:
        # I-1. 종료
        return
    # II. 기존의 멀티탭에 해당 용품이 없을 경우
    # II-1. 기존의 멀티탭에서 다시 쓰지 않을 것으로 바꿔야함
    else:
        value = []
        # II-2. k번째 부터 총 K까지 돌면서 이미 나온 것들은 value에 append한다.
        for i in range(k,K):
            if arr[i] in stack and arr[i] not in value:
                value.append(arr[i])
        # II-3. 순회가 끝났을 경우 len(value)가 N보다 작다면 not in value를 찾아서 교환한다
        if len(value) <N:
            for j in range(N):
                if stack[j] not in value:
                    stack[j] = n
                    break
        # II-4. 순회가 끝났을 경우 len(value)==N이면 value 맨뒤에 있는 값의 stack.index로 찾아 바꾼다.
        elif len(value) == N:
            temp = stack.index(value[-1])
            stack[temp] = n
        cnt +=1

N,K = map(int,input().split())
arr = list(map(int,input().split()))
#stack=[]에 append하여 len값이 N이 될때 까지 진행하여 중복된 값이 없는 stack을 만든다.
stack =[]
k = 0
cnt = 0
start_idx = 0
while len(stack)<N:
    if arr[k] not in stack:
        stack.append(arr[k])
        start_idx +=1
    k +=1
for i in range(start_idx,K):
    MultiTap(arr[i],i)
print(cnt)


