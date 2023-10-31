T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    arr.append(0)                                   #n-1 인덱스 까지 고려해야하니 추가 해서 고려
    long_stem = 1                                   #제일 긴 줄기
    sweet_potato = 0                                #긴 줄기의 고구마 수
    max_sweet_potato = 0                            #제일 긴 줄기의 고구마 수
    stem = 1                                        #긴 줄기
    cnt = 0

    for i in range(N):
        if arr[i]<arr[i+1]:
            stem +=1
            sweet_potato +=arr[i]
        else:
            if stem >1:                             #1보다 크다면 긴 줄기였다는 뜻이니 줄기와 고구마수 추가함
                sweet_potato +=arr[i]
            if long_stem < stem:
                long_stem = stem
                max_sweet_potato = sweet_potato
            if long_stem == stem:                   #줄기가 같다면 고구마 수로 비교
                if max_sweet_potato <sweet_potato:
                    max_sweet_potato =sweet_potato
            if stem >1:
                cnt +=1
            stem = 1
            sweet_potato = 0
    print(f'#{tc} {cnt} {max_sweet_potato}')

