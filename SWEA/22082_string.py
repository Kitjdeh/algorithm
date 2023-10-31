import sys

sys.stdin = open('22082_string.txt')

#문자열을 숫자열로 변경 --> 숫자를 문자로 변경
#a = {"ZRO":0, "ONE":1, "TWO":2,"THR":3,"FOR":4,"FIV":5,"SIX":6,"SVN":7,"EGT":8,"NIN":9}

a = ["ZRO","ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for t in range(1,T+1):
    tc, N = input().split()
    N = int(N)
    target = []
    arr = list(input().split())
    for i in a:
        for j in arr:
            if i == j:
                target.append(i)
    print(tc)
    print(" ".join(target))

