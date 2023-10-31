import sys
sys.stdin = open('계산기3.txt')
cal = ['+','*']                 #연산자 +.*
cir = ['(',')']                 #우선 연산자 (,)
'''
(가 시작하면 +1 )가 나오면 -1을 넣어 우선순위 중첩의 max값을 파악한다.
max 값이 시작 할 경우 그 안의 숫자들을 다시 *,+로 만들어 계산하는 함수 f를 만든다

'''
for tc in range(1,11):
    N = int(input())
    char = input()
    for i in range(N):
        temp = 0
        if char[i] =='(':
            temp += 1
        elif char[i] ==')':

        elif char[i] in cal:

        else:
            char[i]
