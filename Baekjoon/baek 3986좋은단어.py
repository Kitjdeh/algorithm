T = int(input())
Tcnt = 0
for tc in range(T):
    char = list(input())
    N = len(char)
    stack = []
    cnt=0
    for i in range(0,N):
        stack.append(char[i])
        if len(stack)>1:
            if stack[-1]==stack[-2]:
                stack.pop()
                stack.pop()
                cnt+=1
    if len(stack) == 0:
        Tcnt +=1
print(Tcnt)
