import sys
sys.stdin = open("220922_완전검색_그리디 화물도크.txt")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(i+1,N):
    #종료 시간 순으로 정렬
            if arr[i][1] > arr[j][1]:
                arr[i],arr[j] = arr[j],arr[i]

    cnt = 1
    end_time =arr[0][1]
    for i in range(1,N):
        if arr[i][0]<end_time:
            pass
        # 종료 시간보다 뒤에서 시작 한다면
        else:
            end_time = arr[i][1]
            cnt +=1
    print(f'#{tc} {cnt}')