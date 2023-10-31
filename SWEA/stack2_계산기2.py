 import sys
sys.stdin = open('수업 자료/stack2_계산기2.txt')
for tc in range(1,11):
    N = int(input())
    arr = input()                       #문자열 받을 arr 생성
    stack =[]                           #계산 숫자열을 받을 stack 생성
    cal=0                               #우선 순위인 *연산자 확인 cal 생성
    result=0
    for i in range(N):
        if arr[i] == '*':
            cal +=1                     #cal 에 + 추가하여 다음 i+1의 숫자가 바로 계산되게 설정
        elif arr[i] =='+':
            continue                    #*연산자들 우선으로 계산 후 연산하여야 하니 conintue
        else:
            stack.append(int(arr[i]))   #int로 바꾸어 append
            if cal>0:                   #앞연산에 *가 있으면 +1되어 자동으로 if조건 만족
                p=stack.pop()
                q=stack.pop()
                r = p*q
                stack.append(r)
                cal += -1
    for i in range(len(stack)):         #우선 연산인 *가 끝났으니 + 연산
        result+= stack[i]
    print(f"#{tc} {result}")
