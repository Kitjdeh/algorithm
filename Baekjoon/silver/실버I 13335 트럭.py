N,w,L = map(int,input().split())
arr = list(map(int,input().split()))
stack = [0] * w                         #길이가 w인 다리
total_weight = 0                        #다리의 전체 하중
cnt = 0
while len(arr) >0:                      #다리 입장 대기중인 트럭 없을 때 까지
    total_weight += -stack[0]           #우선 다리에서 트럭 하나가 빠져야함
    stack.pop(0)
    k = arr[0]                          #입장대기 트럭
    if total_weight + k >L:             #얘가 입장하면 하중을 넘길경우
        stack.append(0)                 #트럭입장 없으니 0을 넣어줌
    else:
        total_weight += k               #하중 문제 없으니 k 추가
        stack.append(arr.pop(0))        #대기트럭에서 제거 하여 stack에 추가
    cnt +=1
#마지막 트럭이 다리에 올라간 후 계속 전진해서 다 빠져나오려면 w만큼 더 가야함
print(cnt+w)