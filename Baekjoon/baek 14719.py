H, W = map(int,input().split())
num = list(map(int,input().split()))
a = list([0]*H for i in range(W))
for i in range(W):
    for j in range(num[i]):
        a[i][j] =1
cnt = 0
for j in range(H):
    for i in range(1,W-1):
        if a[i][j] == 0 and a[i-1][j] ==1:
#w까지 벽돌이 있는지(=1) 확인하는 for 문 작성
            ch = 0
            L = W-i
            for k in range(1,L):
                if a[i+k][j] == 1:
                    ch += 1
            if ch != 0 :
                a[i][j]=1
                cnt +=1
            else:
                break
print(cnt)

