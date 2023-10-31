import sys
sys.stdin = open('6일차 피자굽기.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    #화덕에 피자를 넣을 때 번호도 같이 넣어준다.
    piz = [[arr[i],i+1] for i in range(M)] #피자에 치즈와 번호와 연동하여 입력
    pot =[]                                #화덕
    for i in range(N):
        pot.append(piz.pop(0))              #화덕pot에 N만큼의 피자를 넣어줌
    k =0
    while len(pot) != 1:                    #화덕에 피자가 하나만 남기 전까지
        hol = pot.pop(0)                    #맨앞의 구멍에서 하나뺀다
        hol[0] //=2
        if hol[0] ==0:                      #치즈가 0이 된 피자가 발생하면
            if piz != []:                   #남은 피자가 있다면
                pot.insert(0,(piz.pop(0)))  #index0 자리에 남은 피자를 화덕에 넣는다.
        else:
            pot.append(hol)                 #치즈가 남았으면 뒤로 보낸다.
    print(f'#{tc} {pot[0][1]}')
