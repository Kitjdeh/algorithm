import sys
sys.stdin = open("의석이의 세로로 말해요.txt")
T = int(input())
for tc in range(1,T+1):
#공백으로 되어있는 15*15의 arr을 만든다
#행과 열을 뒤바꾼다
#공백을 뺀 후 출력
    a=[]
    result=[]
    arr = [[" "]*15 for i in range(15)]
    for _ in range(5):
        a.append(list(input()))
    for i in range(5):
        for j in range(len(a[i])):
            arr[j][i] = a[i][j]
    #arr에 덧씌우며 i와j 순서를 바꾸어줌
    for k in range(15):
        num=[]
        num="".join(arr[k])
        num=''.join(num.split())
        result.append(num)
    print(f'#{tc} {"".join(result)}')



