import sys

sys.stdin = open('9일차 - 사칙연산.txt')
cal = ['/','+','-','*']
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        if Tree[n] == '/':
            Tree[n] = Tree[ch1[n]] / Tree[ch2[n]]
        elif Tree[n] == '*':
            Tree[n] = Tree[ch1[n]] * Tree[ch2[n]]
        elif Tree[n] == '+':
             Tree[n] = Tree[ch1[n]] + Tree[ch2[n]]
        elif Tree[n] == '-':
            Tree[n] = Tree[ch1[n]] - Tree[ch2[n]]
        return Tree[n]


for tc in range(1,11):
    N = int(input())
    Tree = [0]*(N+1)
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    par = [0]*(N+1)
    cnt = 0
    cal_order=[]
    for i in range(1,N+1):
        arr = list(input().split())
        if arr[1] in cal:
            ch1[i] = int(arr[2])
            ch2[i] = int(arr[3])
            par[ch1[i]] = i
            par[ch2[i]] = i
            Tree[i] = arr[1]
            cnt +=1
        else:
            Tree[i] = int(arr[1])
    postorder(1)
    print(f'#{tc} {int(Tree[1])}')

    # if Tree[n] == '/':
    #     Tree[n] = float(ch1[n]) / float(ch2[n])
    # elif Tree[n] == '*':
    #     Tree[n] = float(ch1[n]) * float(ch2[n])
    # elif Tree[n] == '+':
    #     Tree[n] = float(ch1[n]) + float(ch2[n])
    # elif Tree[n] == '-':
    #     Tree[n] = float(ch1[n]) - float(ch2[n])
    # return Tree[n]

    # def calculator(N):
    #     if Tree[N] == '/':
    #         Tree[N] = float(ch1[N]) / float(ch2[N])
    #     elif Tree[N] == '*':
    #         Tree[N] = float(ch1[N]) * float(ch2[N])
    #     elif Tree[N] == '+':
    #         Tree[N] = float(ch1[N]) + float(ch2[N])
    #     elif Tree[N] == '-':
    #         Tree[N] = float(ch1[N]) - float(ch2[N])

    # print(cal_order)
    # for i in range(N):
    #     n = cal_order.pop(0)
    #     if Tree[n] == '/':
    #         Tree[n] = float(ch1[n]) / float(ch2[n])
    #     elif Tree[n] == '*':
    #         Tree[n] = float(ch1[n]) * float(ch2[n])
    #     elif Tree[n] == '+':
    #         Tree[n] = float(ch1[n]) + float(ch2[n])
    #     elif Tree[n] == '-':
    #         Tree[n] = float(ch1[n]) - float(ch2[n])








