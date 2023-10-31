#I. 레프리콘을 만날경우함수 LEP(소지금,기준값)생성
#II. 트롤을 만날 경우 함수 Troll(소지금,기준값)생성
#II-1. 해당 방을 넘어가지 못할 경우 status값을 0으로 변경
#III-0. n이 0이 input 된다면 break
#III-1. 위치 이동의 경우 소지금 money, 현재 방 번호 n을 설정
#III-2. E,L,T의 각 경우 마다 소지금 money,n을 출력
#III-3. 각 케이스의 while 문 생성



def LEP(money,standard):
    if money > standard:
        return money
    else:
        money = standard
        return money

def Troll(money,standard):
    global status
    if money >= standard:
        money += -standard
        return money
    else:
        status = 0
        money = -1
        return money

def f(type,n,money):
    if type == 'L':
        money = LEP(money,arr[n-1][1])
        visited[n-1]=1
    elif type == 'E':
        n = arr[n-1][2]


while True:
    N = int(input())
    #III-0
    if N == 0:
        break
    else:
        money = 0
        arr=[0]*N
        visited = [0]*N
        status = 1
        n = 1
        for i in range(N):
            temp = list(input().split())
            arr[i] = [temp[0],int(temp[1]),int(temp[2]),int(temp[3])]
        # while status:
        #     print(visited,money,status,n)
        #     if visited[n-1] == 1 or visited[N-1]==1:
        #         break
        #     if arr[n-1][0] == 'L':
        #         money = LEP(money,arr[n-1][1])
        #         visited[n-1]=1
        #         n = arr[n-1][2]
        #     elif arr[n-1][0] == 'T':
        #         money = Troll(money,arr[n-1][1])
        #         visited[n - 1] = 1
        #         if money <0:
        #             break
        #         n = arr[n-1][2]
        #     elif arr[n-1][0] == 'E':
        #         visited[n - 1] = 1
        #         n = arr[n-1][2]
        # if visited[N-1] == 1 and status == 1:
        #     print('Yes')
        # else:
        #     print('No')
        while True:
