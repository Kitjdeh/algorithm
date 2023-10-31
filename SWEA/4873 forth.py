import sys
sys.stdin = open('forth.txt')
cal = ['/','*','+','-']
T = int(input())
for tc in range(1,T+1):
    char = list(input().split())
    stack =[]
    arr =[]
    N = len(char)
    for i in range(N):
        if char[i] in cal:
            if len(stack)<2:
                stack.append(1)
                stack.append(2)
                break
            q = stack.pop()
            p = stack.pop()
            if char[i] =='*':
                r = p*q
                stack.append(r)
            elif char[i] =='/':
                r = p//q
                stack.append(r)
            elif char[i] == '+':
                r = p+q
                stack.append(r)
            else:
                r = p-q
                stack.append(r)

        elif char[i] =='.':
            continue
        else:
            t = int(char[i])
            stack.append(t)
    if len(stack) > 1:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {stack[0]}')