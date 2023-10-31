import sys
sys.stdin = open('간단한 소인수 분해.txt')
def f(N,t):                                 #N이 t로 나누어 떨어질 경우 몇제곱인지 확인
    cnt = 0
    while True:
        if N%t ==0:
            N //=t
            cnt +=1
        else:
            break
    return cnt
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a= f(N,2)
    b= f(N,3)
    c= f(N,5)
    d= f(N,7)
    e= f(N,11)
    print(f"#{tc} {a} {b} {c} {d} {e}")