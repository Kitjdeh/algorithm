import sys

sys.stdin = open('swea4864.txt')

T = int(input())
for tc in range(1,T+1):
    str1 = input()
    N = len(str1)
    str2 = input()
    M = len(str2)
    count = 0
    for i in range(M-N+1):
        if str1 == str2[i:i+N]:
            count +=1
            break
    if count ==1:
        print(f'#{tc} 1')
    elif count ==0:
        print(f'#{tc} 0')
