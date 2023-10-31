import sys

sys.stdin = open('color2.txt')
T = int(input())
for t in range(1,T+1):
    N = int(input())
    #red 의 칸, blue의 칸을 적을 리스트
    red=[]
    blue=[]
    share=[]
    area=0
        #N개의 테스트 케이스가 추가
    for _ in range(N):
        x1,y1,x2,y2,c = list(map(int,input().split()))
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if c == 1:
                    red.append([i,j])
                elif c ==2:
                    blue.append([i,j])
    for i in red:
        if i in blue:
            share.append(i)
    if share==blue:
        

    for _ in range(N):
        x1,y1,x2,y2,c = list(map(int,input().split()))
        area += 2*(x2-x1+1+y2-y1+1)


    print(f'#{t} {area}')
    '''
        #N개의 테스트 케이스가 추가
    for _ in range(N):
        x1,y1,x2,y2,c = list(map(int,input().split()))
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if c == 1:
                    red.append([i,j])
                elif c ==2:
                    blue.append([i,j])  
    '''
