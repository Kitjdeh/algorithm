#가능한 결과 려면
#1. 승의 총합 = 패의 총합
#2. 한 국가의 승/무/패 총합 = 5
#3. 1번조건 && 2번 조건 둘다 만족하여야 한다.
#4. 1번조건을 확인하는 for문 / 2번 조건을 만족하는 for문/

#1. 총 30번의 경기를 치른다 -> a팀의 1승 / b팀의 1패 를 쳐내거나 c팀의 무승부/d팀의 무승부 쳐내는걸 30번 한다.
#2. team 리스트에 승,무,패 만큼 각각 'w' / 'd' / 'l' 을 추가한다.
#3.
# result = []
# truth = 0
arr = list(map(int,input().split()))
team = [[ ] for i in range(6)]
win = []
draw = []
lose = []
for i in range(6):
    team.append(arr[3*i])
    draw.append(arr[3*i+1])
    lose.append(arr[3*i+2])


# cnt = 0
#     if win[i]+lose[i]+draw[i] != 5:
#         truth +=1
# while cnt !=15:
#     win_cnt = 0
#     lose_cnt = 0
#     for i in range(6):
#         if win[i] >0:
#             w= i
#             break
#         win_cnt +=1
#     for i in range(6):
#         if lose[i] >0 and w != i:
#             l = i
#             break
#         lose_cnt +=1
#     if

a=[1,2,3,4]
a.append('1'*5)
print(a)
# for _ in range(4):
#     #3
#     truth = 0
#     win = 0
#     lose = 0
#     draw = 0
#     arr = list(map(int,input().split()))
#     for i in range(6):
#         win +=arr[i*3]
#         lose +=arr[i*3+2]
#         draw +=arr[i*3+1]
#         if arr[i*3]+arr[i*3+1]+arr[i*3+2] !=5:
#             truth +=1
#     if win == lose:
#         pass
#     else:
#         truth +=1
#     if truth >0:
#         result.append('0')
#     elif truth == 0:
#         result.append('1')
# result = " ".join(result)
# print(result)
