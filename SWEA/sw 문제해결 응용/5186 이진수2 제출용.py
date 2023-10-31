import sys
sys.stdin = open("5186 이진수2 제출용.txt")
T= int(input())
def bit_and(n):
    result = ''
    i = 1
    while n:
        if 2**(-i) <= n:
            n += -2**(-i)
            i += 1
            result += '1'
        else:
            result += '0'
            i +=1
        if n ==0:
            break
        elif i ==13 and n !=0 :
            # result = 'overflow'
            break

    return result


for tc in range(1,T+1):
    N = input()
    N = float(N)
    print(f'#{tc} {bit_and(N)}')


    #
    # N = float(N)
    # output=''
    # for i in range(1,-12,-1):
    #     if N & (1<<i):
    #         output += '1'
    #     else:
    #         output += '0'
    # return output
    #
    # print(bit_and(input()))