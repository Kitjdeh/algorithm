import sys

sys.stdin = open('색칠하기2.txt')
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
    #blue와 red 의 교집합 확인하여 share 리스트 추가
    for i in red:
        for j in blue:
            if i == j:
                share.append(i)
    #share로red blue 공통부분 제거
    for i in red:
        for j in share:
            if i == j:
                red.remove(i)
    for i in blue:
        for j in share:
            if i ==j:
                blue.remove(i)
    #x값y값으로 둘레 길이 정하기








    #for _ in range(N):
     #   x1,y1,x2,y2,c = list(map(int,input().split()))
      #  area += 2*(x2-x1+1+y2-y1+1)



    #print(f"#{t} {area}")
