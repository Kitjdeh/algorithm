def msort(i,N):# i: 병합 구간의 시작 인덱스 N: 구간의 원소 개수 L = i, r= i+N-1
    global cnt
    if N ==1:   #분할한 원소가 1개만 남은 경우
        return
    else:
        msort(i,N//2)       #병합할 왼쪽 구간의 시작 인덱스
        msort(i+N//2, N//2) #병합할 오른쪽 구간의 시작 인덱스
        # 리턴 값 없이 i, j = i+N//2 계산으로 가능
        if arr[i+(N//2)-1] > arr[i+N-1]:  #문제에서 요구하는 두번 째 출력
            cnt +=1
        k = 0
        l,r = i ,i+N//2
        while l <i+N//2 and r < i+N:     #i왼쪽 구간에서 비교할 위치, j 오른쪽 구간에서 비교할 위치
            if arr[l] > arr[r]:      #오름차순, 작은 숫자 먼저 tmp 에 복사
                tmp[k] =arr[l]
                l += 1               # 왼쪽 구간에서 선택된 경우 i++
            else:
                tmp[k] = arr[r]
                r += 1              #오른쪽 구간에서 선택된 경우 j++
            k += 1
        while l<i+N//2:             #왼쪽 구간에 남은 숫자가 있으면 모두 tmp 에 복사
            tmp[k] = arr[l]
            l += 1
            k += 1
        while r <i+ N:
            tmp[k] = arr[r]
            r +=1
            k +=1
        for k in range(N):          # 병합한 결과를 원본에 복사
            arr[i+k] = tmp[k]
        return i