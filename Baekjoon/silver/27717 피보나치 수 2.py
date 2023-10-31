#재귀호출 f(n)의 경우
# n
# n-1 / n-2
# n-2 n-3 / n-3 n-4
# n-3 n-4 / n-4 n-5 / n-4 n-5 / n-5 n-6 ....
# n이 최소값인 2가 될때까지 n-2번 쪼개짐
#

def fib(n):
    for i in range(n-2):
        num.append(num[-1]+num[-2])
        num.pop(0)
    return num[-1]
def fibonacci(n):
    cnt = 2
    temp = 0
    for i in range(n-4):
        temp = arr[-1]
        arr[-1]=(arr[-1]+arr[-2])
        arr[-2]=temp

        cnt +=1
    print(arr[-1]%1000000007, cnt)
arr = [2,3]

import sys
N = int(sys.stdin.readline())
fibonacci(N)