#I. 9개의 가로줄,세로줄, 3x3박스 총 27개의 1~9 리스트를 가져야 함.
#II. arr[i][j]에 들어갈 값을 찾는 함수 sudoku(i,j) 생성
#1-1. 이 함수는 해당 칸이 0이 아니면 종료
#1-2. 해당 칸이 0일 경우 작동 시작
#2. []의 check리스트 생성
#3-1. 가로줄 부터 k값이 존재하면 check에 append
#3-2. 세로줄도 동일하게 적용 이미 존재하는 값이면 pass
#3-3. arr[i][j]box 카운팅
#4. len(check) ==8 이면 나머지 한개를 찾아서 arr[i][j] 완성
#5. 안된다면

# def sudoku(x,y):
#     global cnt
#     if arr[x][y] !=0:
#         cnt +=1
#         return
#     # 1-2. 해당 칸이 0일 경우 작동 시작
#     elif arr[x][y]==0:
#         # 2. []의 check리스트 생성
#         check = []
#         #3-1. 가로줄 부터 k값이 존재하면 check에 append
#         for i in range(9):
#             if i !=x and arr[x][i] !=0 and arr[x][i] not in check:
#                 check.append(arr[x][i])
#         # 3-2. 세로줄도 동일하게 적용 이미 존재하는 값이면 pass
#         for j in range(9):
#             if j !=y and arr[j][y] !=0 and arr[j][y] not in check:
#                 check.append(arr[j][y])
#         if len(check) ==8:
#             for i in range(1,10):
#                 if i not in check:
#                     break
#             arr[x][y]= i
#             cnt +=1
#             return
#         else:
#             for i in range(3):
#                 for j in range(3):
#                     p,q= x//3*3+i,y//3*3+j
#                     if p != x or q !=y:
#                         if arr[p][q] not in check and arr[p][q] !=0:
#                             check.append(arr[p][q])
#             # 4. len(check) ==8 이면 나머지 한개를 찾아서 arr[i][j] 완성
#             if len(check) ==8:
#                 for i in range(1, 10):
#                     if i not in check:
#                         break
#                 arr[x][y] = i
#                 cnt +=1
#             return
# #경우의 수 넣어보는 함수
# def may(i,j):
#      return
#
# cnt = 0
# arr = [0]*9
# for i in range(9):
#     arr[i] = list(map(int,input().split()))
# # print(arr)
# while cnt <81:
#     cnt = 0
#     for i in range(9):
#         for j in range(9):
#             sudoku(i,j)
#
# for i in range(9):
#     print(" ".join(map(str,arr[i])))
# 0 0 3 4 5 6 7 8 9
# 4 5 6 7 8 9 0 0 3
# 7 8 9 0 0 3 4 5 6
# 0 0 4 3 6 5 8 9 7
# 3 6 5 8 9 7 0 0 4
# 8 9 7 0 0 4 3 6 5
# 5 3 0 6 4 0 9 7 8
# 6 4 0 9 7 8 5 3 0
# 9 7 8 5 3 0 6 4 0
 #3-1. 가로줄 부터 k값이 존재하면 check에 append
#         for i in range(9):
#             if i !=x and arr[x][i] !=0 and arr[x][i] not in check:
#                 check.append(arr[x][i])
#         # 3-2. 세로줄도 동일하게 적용 이미 존재하는 값이면 pass
#         for j in range(9):
#             if j !=y and arr[j][y] !=0 and arr[j][y] not in check:
#                 check.append(arr[j][y])
#  for i in range(3):
#                 for j in range(3):
#                     p,q= x//3*3+i,y//3*3+j
#                     if p != x or q !=y:
#                         if arr[p][q] not in check and arr[p][q] !=0:
#                             check.append(arr[p][q])
#I.[i,j]에 k를 넣는 함수 sudoku(i,j) 생성
#II-1. [i,j]의 가로, 세로 box에서 나오지 않은 숫자 리스트 temp=[a,b,c,,,,]를 생성
#II-2. arr[i][j] = a 로 두고 재귀
#II-3. 끝나면 다시 arr[i][j] = 0

def sudoku(x,y,arr):
    check_box[x][y] = []
    temp =[]
    if arr[x][y] == 0:
        #세로 축에 있는 다른 숫자들 확인
        for i in range(9):
            if  arr[x][i] !=0 and arr[x][i] not in temp:
                temp.append(arr[x][i])
        #가로 축에 있는 다른 숫자들 확인
        for j in range(9):
            if  arr[j][y] !=0 and arr[j][y] not in temp:
                temp.append(arr[j][y])
        #현재 박스 기준 다른 숫자들 확인
        for i in range(3):
            for j in range(3):
                p,q = x//3*3+i,y//3*3+j
                if arr[p][q] not in temp and arr[p][q] !=0 and (x !=p and y !=q):
                    temp.append(arr[p][q])
        # 현재 나온 숫자가 9개면 1~9 다 나온거니 이 턴은 나가리
        if len(temp) ==9:
            return
        # 9가 아니면 가능한 숫자들이 있다는 뜻 / check_box[x][y]에 저장
        else:
            for i in range(1,10):
                if i not in temp:
                    # check.append(i)
                    check_box[x][y].append(i)
    else:
        check_box[x][y].append(arr[x][y])
    if x == 0 and y == 1 and 1 in check_box[x][y]:
        print(111, check_box[x][y], arr)
    # print(x,y,temp)
    # check_box에 있는 것들을 돌아가며 arr[x][y]에 넣어 보고
    for j in check_box[x][y]:
        arr[x][y] = j
        # print(x,y,check_box[x][y],j)
        if x == 8 and y == 8:
            tmp =[[] for _ in range(9)]
            for t in range(9):
                tmp[t] = arr[t][:]
            result.append(tmp)
            return
        else:
            if y < 8:
                sudoku(x,y+1,arr)
            else:
                sudoku(x+1,0,arr)
    # print(x,y)
    # if x == 8 and y == 8:
    #     tmp = arr[:]
    #     result.append(arr)
    #     return
    # else:
    #     if y < 8:
    #         sudoku(x, y + 1)
    #     elif y == 8:
    #         sudoku(x + 1, 0)
cnt = 0
arr = [0]*9
for i in range(9):
    arr[i] = list(map(int,input().split()))
check_box = [[[]*9 for _ in range(9)] for _ in range(9)]
result=[]
sudoku(0,0,arr)
# print(result[0])
L = len(result)
for i in range(9):
    print(" ".join(map(str,result[0][i])))
