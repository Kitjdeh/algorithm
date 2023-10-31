def bisort(l, r, b, m):
    global cnt
    if b == A[m]:  # b가 m에 있으면 종료
        cnt += 1
        return
    elif b > A[m]:
        l = m + 1
        m = (l + r) // 2
        if b > A[m]:  # 오른쪽 다음 오른쪽은 아니니 종료
            return
        else:
            bisort(l, r, b, m)  # 오 - 왼 이니 진행
    elif b < A[m]:
        r = m - 1
        m = (l + r) // 2
        if b < A[m]:  # 왼쪽 -> 왼족 이니 종료
            return
        else:
            bisort(l, r, b, m)  # 왼 - 오 이니 진행

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(M):
        bisort(0, N - 1, B[i], (N - 1) // 2)
    print(f'#{tc} {cnt}')