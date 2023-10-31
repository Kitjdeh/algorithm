# import sys
# sys.setrecursionlimit(10**6)
import sys
sys.stdin = open("2일차 - 최대상금.txt")
def order(t,r):                                             #r번 섞을때 나올 수 있는 경우의 수
    global ord
    global max_ans
    N = len(num)
    if t == r:
        ans = int(''.join(num))
        if ans > max_ans:
            max_ans = ans
        ord.append(num[0::])
        return
    else:
        for i in range(N):
            for j in range(i+1,N):
                num[i],num[j] = num[j],num[i]
                order(t+1,r)
                num[i], num[j] = num[j], num[i]

T = int(input())
for tc in range(1,T+1):
    num, r = input().split()
    num = list(num)
    N = len(num)
    ord = []
    r = int(r)
    if r <3:
        max_ans = 0
        order(0,r)
        print(f'#{tc} {max_ans}')
    else:
        #수어진 숫자가 가장 큰 경우 그 숫자를 목표로 바꿔 가는 방식
        max_num = num[0::]                  # 목표로 하는 가장 큰수
        for i in range(N):                  # 숫자 배열 정렬
            for j in range(i + 1, N):
                if max_num[i] < max_num[j]:
                    max_num[i], max_num[j] = max_num[j], max_num[i]
        double = 0                              # 중복인 수 가 있으면 가장 큰 수로 만든 후 중복된 수만 바꾸면 되니 더이상 숫자 변경X
        for i in range(N-1):
            if max_num[i]==max_num[i+1]:
                double +=1
        cnt = 0
        t = 0
        while cnt != r:
            if t >= N-1 and double ==0:         #중복인 수가 없고 cnt가 남았으면 맨뒤2개만 계속 바꿔줌
                num[-1], num[-2] = num[-2], num[-1]
                cnt += 1
                t = N
            elif t > N-1 and double>0:
                cnt +=1
            elif num[t] != max_num[t] and t <N-1:
                for i in range(N-1,-1,-1):
                    if num[i] == max_num[t]:
                        num[i],num[t] = num[t],num[i]
                        cnt +=1
                        t +=1
                        break
            else:
                t +=1
        print(f'#{tc} {"".join(num)}')

