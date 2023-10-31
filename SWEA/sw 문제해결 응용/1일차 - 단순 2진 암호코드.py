import sys
sys.stdin = open("1일차_단순 2진 암호코드.txt")
ps_map = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9
}
def ps_ch(a):
    global M
    t = M-1
    result=[]
    while t > -1:
        if a[t] == '0':
            t += -1
        else:
            P = ps_map.get(f'{a[t-6:t+1]}')
            if P == None:
                t += -7
            else:
                result.append(P)
                t += -7
    if len(result) == 8:
        return result[::-1]
    # for i in range(M-1,54,-1):
    #     if a[i] == '1':
    #         P = ps_map.get(f'{a[i-7:i+1]}')
    #         if P != None:
    #             result.append(P)
    # if len(result) == 8:
    #     return result
def check_code(a):
    global K
    A=0
    B=0
    for i in range(0,8,2):
        A +=a[i]
    for j in range(1,8,2):
        B +=a[j]
    if (3*A+B)%10 == 0:
        K = A+B
        return K
    else:
        return 0

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [0]
    while True:
        R = ps_ch(input())
        if R != None:
            arr[0]= R
            print(arr)
        break
    L = len(arr)
    if check_code(arr[0]) != 0:
        print(f'#{tc} {check_code(arr[0])}')
    else:
        print(f'#{tc} 0')