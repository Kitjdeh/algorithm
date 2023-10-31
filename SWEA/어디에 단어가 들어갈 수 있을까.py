import sys
sys.stdin = open('어디에 단어가 들어갈 수 있을까.txt')
T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    a = [0]*N
    for i in range(N):
        a[i] = list(map(int,input().split()))
    cnt = 0
    for i in range(N):                          #가로 방향으로 빈공간 길이 모음 수집
        t = 0
        s = 0
        while t != N:
            if a[i][t] ==1:                     #1(빈칸인 경우)
                s +=1                           #채울 수 있는 블럭 길이(s)가 +1
                t +=1                           #다음칸 봐야 하니 t+1
                if t ==N and s ==K:             #다음칸이 막혀있고 조건에 맞으면
                    cnt +=1
            else:
                t +=1
                if  s == K:
                    cnt +=1
                s = 0
    for i in range(N):                           # 세로로 방향으로 빈공간 길이 모음 수집
        t = 0
        s = 0
        while t != N:
            if a[t][i] ==1:                     #1(빈칸인 경우)
                s +=1                           #채울 수 있는 블럭 길이(s)가 +1
                t +=1                           #다음칸 봐야 하니 t+1
                if t ==N and s ==K:             #다음칸이 막혀있고 조건에 맞으면
                    cnt +=1
            else:
                t += 1
                if s == K:
                    cnt += 1
                s = 0
    print(f"#{tc} {cnt}")


