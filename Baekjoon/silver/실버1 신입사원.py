from sys import stdin
input = stdin.readline
T= int(input())
for tc in range(1,T+1):
    N = int(input())
    man_list = [0]*(N)
    score=[0]*(N+1)
    fail_cnt = 0
    cut_line = [N,N]
    for i in range(N):
        fir,sec = map(int, input().split())
        if fir <cut_line[0] and sec < cut_line[1]:
            cut_line = [fir,sec]
        man_list[i] = [fir,sec]
    for i in range(N):
        if man_list[i][0] > cut_line[0] and man_list[i][1] > cut_line[1]:
            fail_cnt +=1
            print(3333,man_list[i])
    print(cut_line)
    print(man_list)
    print(N-fail_cnt)
#     fail_list =[0]*N
#     for i in range(N):
#         for j in range(i+1,N):
#             if man_list[i][0] > man_list[j][0] and man_list[i][1] > man_list[j][1]:
#                 if fail_list[i] == 0:
#                     fail_list[i] = 1
#                     fail_cnt +=1
#             elif man_list[i][0] < man_list[j][0] and man_list[i][1] < man_list[j][1]:
#                 if fail_list[j] == 0:
#                     fail_list[j] = 1
#                     fail_cnt +=1
#     print(N-fail_cnt)
# from sys import stdin
# input = stdin.readline
# for tc in range(1,T+1):
#     N = int(input())
#     man_list = [0]*(N)
#     fail_cnt = 0
#     for i in range(N):
#         man_list[i] = list(map(int,input().split()))


