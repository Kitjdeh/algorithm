import sys
sys.stdin = open("Baby-gin_완전검색_그리디.txt")
T = int(input())
def order(A):                                   #정렬함수
    for i in range(5):
        I = i
        for j in range(i+1,6):
            if A[i]>A[j]:
                I = j
        A[I],A[i] = A[i],A[I]
def triple(A):                                  #3개 중복일시 카운트 및 해당 숫자 제거 함수
    global result
    cnt = 1
    pop_list=[]
    for i in range(len(A)-1):
        if A[i] ==A[i+1]:
            cnt +=1
        else:
            cnt = 1
        if cnt ==3:
            pop_list.append(A[i])
            cnt = 1
            result +=1
    for i in range(len(pop_list)):
        for _ in range(3):
            A.remove(pop_list[i])
    return A
def run(A):                                     #연속 일 경우 카운트 및 해당 숫자 제거 함수
    global result
    cnt= 1
    pop_list = []
    for i in range(len(A)-1):
        if A[i] == A[i+1]-1:
            cnt +=1
        else:
            cnt = 1
        if cnt ==3:
            pop_list.append(A[i])
            cnt =1
            result +=1
    for i in range(len(pop_list)):
        for k in range(-1,2):
            A.remove(pop_list[i]+k)
    return A
for tc in range(1, T+1):
    card = list(map(int,input()))
    order(card)
    result = 0
    A = triple(card)
    B = run(A)
    if result ==2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')