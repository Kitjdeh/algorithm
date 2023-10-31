import sys
sys.stdin = open("2일차 - 최대상금.txt")

T = int(input())
for tc in range(1,T+1):
    num, r = input().split()
    num = list(map(int,num))
    r = int(r)
    max_ans = 0
    max_num = num[0::]
    max_num.sort(reverse=True)              # 목표로 하는 가장 큰수
    N = len(num)
    double = 0
    for i in range(N-1):
        if max_num[i]==max_num[i+1]:
            double +=1
            fir_idx,sec_idx = i,i+1
    cnt = 0
    t = 0

    while cnt != r:
        if t >= N-1 and double ==0:
            num[-1], num[-2] = num[-2], num[-1]
            cnt += 1
            t = N
        elif t > N-1 and double>0:
            num[fir_idx],num[sec_idx] = num[sec_idx],num[fir_idx]
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

    print(tc , num)
# 10
# 123 1
# 2737 1
# 757148 1
# 78466 2
# 32888 2
# 777770 5
# 436659 2
# 431159 7
# 112233 3
# 456789 10