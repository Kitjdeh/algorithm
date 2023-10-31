import sys
sys.stdin = open('swea4866 괄호검사.txt')
T = int(input())
for tc in range(1,T+1):
    char = input()
    n = len(char)
    stack =[]
    for i in range(n):                              #특수문자들 거르는 작업
        if char[i] == '{':
            stack.append(char[i])
        if char[i] == '}':
            stack.append(char[i])
        if char[i] == '(':
            stack.append(char[i])
        if char[i] == ')':
            stack.append(char[i])
        if len(stack)>1:                            #길이가 1이나 0이면 실행 필요X
            if stack[-1]=='}' and stack[-2]=='{':
                stack.pop()
                stack.pop()
            elif stack[-1]==')' and stack[-2]=='(':
                stack.pop()
                stack.pop()
    if len(stack) == 0:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")