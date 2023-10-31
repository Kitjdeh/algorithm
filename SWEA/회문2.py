import sys
sys.stdin = open('회문2.txt')
for tc in range(1,11):
    t = int(input())
    arr = [list(input()) for i in range(100)]
#가로줄 i번째에서 길이 100인 회문이 존재확인
#없으면 99인 회문 존재 확인
#존재하지 않으면 다음 i+1번째 줄 확인 반복
    max_N=1
    for i in range(100):
#k는 매번 가로 줄 갱신마다 100부터 시작해야함
        N = 1
        k = 100
        cnt = 0
#k값을 100부터 시작하여 얼마나 진행할지 모르니 while문으로 진행
#k값이 N보다 작으면 진행 의미가 없으니 while문 조건으로 사용
        while k>max_N:
# 길이가  k 일 때 101-k번 확인해야함
            for j in range(0,100-k+1):
                ch=arr[i][j:j+k]
                if ch ==ch[::-1]:
                    N = k
                    if max_N<N:
                        max_N=N
#확인하였으니 for 문 종료
                    break
            k += -1

#동일하게 세로 확인
    for i in range(100):
        ch =[]
        for j in range(100):
            ch.append(arr[j][i])
        N = 1
        k = 100
        while k>max_N:
            for t in range(0,100-k+1):
                ch1=ch[t:t+k]
                if ch1 ==ch1[::-1]:
                    N = k
                    if max_N<N:
                        max_N=N
                    break
            k += -1

    print(f"#{tc} {max_N}")
