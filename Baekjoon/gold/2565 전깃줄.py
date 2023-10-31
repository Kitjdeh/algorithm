N = int(input())
arr = [0]*N
for i in range(N):
    arr[i] = list(map(int,input().split()))
#전체 중복 수가 0이 된다면 그 값을 출력
max_cnt = 0
max_line = 0
cut_count = 0
arr.sort()
while True:
    max_cnt = 0
    overindex=[0]
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr)):
            if arr[i][0]<arr[j][0] and arr[i][1]>arr[j][1]:                 #중복 조건은 a타워와 b타워의 대소차이가 반대일 경우임
                cnt +=1
            elif arr[i][0]>arr[j][0] and arr[i][1]<arr[j][1]:
                cnt +=1
        if max_cnt<cnt:
            max_cnt=cnt
            max_line=i
            overindex[0]= i
        elif max_cnt == cnt: #값이 같은 경우 max 값끼리 충돌하는 선인지 확인
            overindex.append(i)
    if max_cnt == 0:
        break
    elif len(overindex)>1:
        count_over = 1000
        for i in overindex:
            cnt = 0
            for j in overindex:
                if arr[i][0] < arr[j][0] and arr[i][1] > arr[j][1]:  # 중복 조건은 a타워와 b타워의 대소차이가 반대일 경우임
                    cnt += 1
                elif arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]:
                    cnt += 1
            if count_over > cnt:
                count_over = cnt
                max_line = i
    arr.pop(max_line)
    cut_count+=1
print(cut_count)

# def comb(arr,i):
#     result = []
#     if i ==1:
#         for i in arr:
#             result.append(i)
#     elif i >1:
#         for i in range()
