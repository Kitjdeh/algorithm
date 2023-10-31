import sys
sys.stdin = open("5185 이진수 제출용.txt")

def bit_and(i):
    output = ''
    for j in range(3,-1,-1):
        output += '1' if i & (1 <<j) else '0'
    return output
T= int(input())
for tc in range(1,T+1):

    N, arr = map(str,input().split())
    N = int(N)
    result = ''
    for i in range(N):
        result += bit_and(int(arr[i],16))
    print(f'#{tc} {result}', end ='')
    print()