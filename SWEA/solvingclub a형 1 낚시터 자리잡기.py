import sys
sys.stdin = open('solvingclub a형 1 낚시터 자리잡기.txt')
def order(i,N):
    global ord
    if i ==N:
        ord.append(P[0::])
        return
    else:
        for j in range(i,N):
            P[i],P[j] = P[j],P[i]
            order(i+1,N)
            P[i],P[j] = P[j],P[i]
#거리를 구하여 result 함수에 append
ord=[]
P = [0,1,2]# 1,2,3배치 순열
order(0,3)
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    area = [i for i in range(1,N+1)]
    gate = [0]*4
    for i in range(1,4):
        gate[i] = list(map(int,input().split()))
    #게이트 정보 입력
    #번호순 정렬 게이트의 각 인원 수 len만큼
    #visited 1~N까지
    #f를 만들어서 배치하는 함수

    #거리를 구하여 result 함수에 append
    ord =[]
    P = [1,2,3]# 1,2,3배치 순열
