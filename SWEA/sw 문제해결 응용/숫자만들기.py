import sys
sys.stdin = open('숫자만들기.txt')
def calculator(numb,B):
    stack =[]
    A = num[0::]
    stack.append(A.pop(0))
    while len(A)!=0:
        a = stack.pop(0)
        b = A.pop(0)
        c = B.pop(0)
        if c ==0:
            b = a+b
        elif c ==1:
            b = a-b
        elif c ==2:
            b = a*b
        elif c ==3:
            b = int(a/b)
        stack.append(b)
    result.append(b)
    return
    # else:
    #     a = A.pop(0)
    #     b = A[0]
    #     c = B.pop(0)
    #
    #     A[0] = b
    #     calculator(A,B)

def blend(A,r):
    L = len(A)
    if r == L-1:
        ord.append(A[0::])
    else:
        for i in range(r,L):
            A[i], A[r] = A[r], A[i]
            blend(A, r + 1)
            A[i], A[r] = A[r], A[i]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    A = list(map(int,input().split()))
    cal =[]
    for i in range(4):
        a = A[i]*[i]
        cal += a
    ord= []
    # print(tc, cal)
    blend(cal,0)
    num = list(map(int,input().split()))
    result =[]
    for i in ord:
        calculator(num,i)
    print(tc,max(result)-min(result))
