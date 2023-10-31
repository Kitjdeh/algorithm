# 문자열 중 문자 t 가 p에서 q 동안 몇개가 있는가?
# 문자열 길이가 20만개 -> 한번 체크로 끝내야함
# 문자열 s 를 리스트로 만든 후 set 철 -> 중복없는 문자열 리스트
# 해당 문자마다 각각 list 로 새엉
# 각 k번째 문자가 p 일 경우
# arr.p[k] +=1
# 나머지는 그대로
import sys


S = list(sys.stdin.readline())
L = len(S)
q = int(sys.stdin.readline())
set_s = set(S)
arr = {}
for i in set_s:
    arr[i] = [0]*L
# first_char = S[0]
# arr[first_char][0] = 1
# for i in range(1,L):
#     char = S[i]
#     for key, value in arr.items():
#         if char == key:
#             arr[key][i] = arr[key][i-1] +1
#         else:
#             arr[key][i] = arr[key][i-1]

for i in range(L):
    char = S[i]
    arr[char][i] = 1
for char in set_s:
    for i in range(1,L):
        arr[char][i] += arr[char][i-1]
for i in range(q):
    char, start, end = sys.stdin.readline().split()
    start, end = int(start), int(end)
    if arr.get(char):
        if start != 0:
            print(arr[char][end]-arr[char][start-1])
        else:
            print(arr[char][end])
    else:
        print(0)