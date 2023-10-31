import sys
sys.stdin = open('swea4873 반복문자 지우기.txt')
T= int(input())
for tc in range(1,T+1):
    char = input()                          #문자열 input
    stack =[]                               #stack 생성
    n = len(char)
    for i in range(n):
        stack.append(char[i])
        if len(stack) >1:                   #index error 방지
            if stack[-1] ==stack[-2]:       #가장 최근 들어온 2개를 비교
                stack.pop()                 #동일하면 지우기
                stack.pop()

    print(f"#{tc} {len(stack)}")
