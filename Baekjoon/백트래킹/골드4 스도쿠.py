#I.[i,j]에 k를 넣는 함수 sudoku(i,j) 생성
#II-1. [i,j]의 가로, 세로 box에서 나오지 않은 숫자 리스트 temp=[a,b,c,,,,]를 생성
#II-2. arr[i][j] = a 로 두고 재귀
#II-3. 끝나면 다시 arr[i][j] = 0
import sys
sys.setrecursionlimit(20000)
def sudoku(x,y):
    temp = []
    check_box =[]
    existing = arr[x][y]
    if arr[x][y] == 0:
        #I-1. 가로줄 확인
        for i in range(9):
            if arr[x][i] != 0 and arr[x][i] not in temp:
                temp.append(arr[x][i])
            if arr[i][y] != 0 and arr[i][y] not in temp:
                temp.append(arr[i][y])
        for i in range(3):
            for j in range(3):
                p,q = x//3*3+i,y//3*3+j
                if arr[p][q] != 0 and arr[p][q] not in temp:
                    temp.append(arr[p][q])
        for t in range(1,10):
            if t not in temp:
                check_box.append(t)
    else:
        existing = arr[x][y]
        check_box.append(arr[x][y])
    if len(check_box) ==0:
        return
    else:
        for w in check_box:
            arr[x][y] =w
            if x ==8 and y ==8:
                tmp = [0]*9
                # print(x,y)
                for i in range(9):
                    tmp[i] = arr[i][:]
                result.append(tmp)
                return
            elif y<8:
                sudoku(x,y+1)
                if existing !=0:
                    arr[x][y] = existing
                    existing =0
            else:
                sudoku(x+1,0)
                if existing !=0:
                    arr[x][y] = existing
                    existing = 0

arr = [0]*9
for i in range(9):
    arr[i] = list(map(int,input().split()))
result=[]
sudoku(0,0)
# print(result)
for i in range(9):
    print(" ".join(map(str, result[0][i])))

# 0 0 3 4 5 6 7 8 9
# 4 5 6 7 8 9 0 0 3
# 7 8 9 0 0 3 4 5 6
# 0 0 4 3 6 5 8 9 7
# 3 6 5 8 9 7 0 0 4
# 8 9 7 0 0 4 3 6 5
# 5 3 0 6 4 0 9 7 8
# 6 4 0 9 7 8 5 3 0
# 9 7 8 5 3 0 6 4 0