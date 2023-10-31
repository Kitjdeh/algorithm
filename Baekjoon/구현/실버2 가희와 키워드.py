# N개의 키워드 중 키워드 k가 사용된 여부확인
# 사용된 키워드의 갯수를 확인
# set 와 dict
# dict로
import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
keyword = {}
cnt = 0
for i in range(N):
    word = input()
    keyword[word] = 0
for i in range(M):
    blog = list(sys.stdin.readline().rstrip().split(','))
    L = len(blog)
    for j in range(L):
        if keyword.get(blog[j]) == 0:
            cnt +=1
            keyword[blog[j]] = 1
    print(N-cnt)
