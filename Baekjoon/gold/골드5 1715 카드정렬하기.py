# N개의 묶음이 있으면 총 N-1번의 묶음이 진행되어야함
# 묶음 더미중 제일 작은 2개를 합쳐야 전체 카운팅이 적어짐
from sys import stdin
input = stdin.readline
N = int(input())
arr = [0]*N
for i in range(N):
    arr[i] = int(input())
arr.sort()                                      #오름차순 정렬
result = 0
for i in range(N-1):
    arr[1] = arr[0]+arr[1]                      #제일 앞 2숫자 함침
    result += arr[1]                            #전체 카운팅 추가
    t = 1
    while t<len(arr)-1:                         #N값은 점점 줄어드니 계산값 수정
        if arr[t] > arr[t+1]:
            arr[t], arr[t+1] = arr[t+1],arr[t]  #합친 숫자의 순서 배열
            t +=1
        else:
            break
    arr.pop(0)                                  #idx 0 과 1 을 합쳐서 1에 넣었으니 0은 삭제
print(result)                                   #for문으로 n-1번 하면 1개 남은 숫자가 전체 합
# from sys import stdin
#
# N = int(stdin.readline())
# cards = [0] * N
# for i in range(N):
#     cards[i] = int(stdin.readline())
# cards.sort()
#
# result = cards[0] + cards[1]  # 정렬해서 가장 작은 값 2개 더하기
# for i in range(2, N - 1):
#     if cards[i] + cards[i + 1] <= result:  # 다음 2개 합이 현재 result보다 작다면
#         tmp = result  # 현재 result를 cards[i+1]에 저장하고서
#         result = cards[i] + cards[i + 1]  # result를 갱신해준다
#         cards[i + 1] = tmp
#
#     else:
#         if cards[i] > cards[i + 1]:
#             cards[i], cards[i + 1] = cards[i + 1], cards[i]
#         result += result + cards[i]
#
# # 출력시에 남은 마지막 값 cards[N-1]을 더해야 한다.
# print(2 * result + cards[N - 1])