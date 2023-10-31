import sys
sys.stdin = open('9일차 - 중위순회.txt')
def root_finder(N):
    for i in range(1,N+1):
        if par[i] ==0:
            return i

#중위순회 함수 설정
def inorder(n):
    global result
    if n:
        inorder(ch1[n])
        result.append(str_idx[n])
        inorder(ch2[n])
#입력값 ch1,ch2,str_idx로 구분
for tc in range(1,11):
    result = []
    N = int(input())
    arr=[]
    str_idx=[0] * (N+1)
    ch1 =[0] * (N+1)
    ch2 =[0] * (N+1)
    for i in range(1,N+1):
        a = list(input().split())
        str_idx[i] = a[1]
        if len(a)==3:                   #len가 3이면 ch1만 보유
            ch1[i] = int(a[2])          #ch1[p] = c 가된다
        elif len(a)==4:                 #len가 4면 ch1,ch2보유
            ch1[i] = int(a[2])
            ch2[i] = int(a[3])
    inorder(1)
    print(f'#{tc} {"".join(result)}')

