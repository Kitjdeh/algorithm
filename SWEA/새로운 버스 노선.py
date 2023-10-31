import sys
sys.stdin = open("새로운 버스 노선.txt")
T = int(input())
for tc in range(1,T+1):
    arr = [0]*1001
    N = int(input())
    max_a=0
    for i in range(N):
        a,b,c = map(int,input().split())
        if a ==1:
            for t in range(b,c+1):
                arr[t] +=1
        elif a ==2:
            for t in range(b,c+1,2):
                arr[t] +=1
        elif a ==3:
            if b%2 ==0:
                for t in range(b,c+1):
                    if t%4==0:
                        arr[t] +=1
            else:
                for t in range(b,c+1):
                    if t%3 ==0 and t%10 !=0:
                        arr[t] +=1
    for i in range(1000):
        if arr[i] >max_a:
            max_a =arr[i]
    print(f'#{tc} {max_a}')