N = int(input())
for tc in range(1,N+1):
    a = list(input().split())
    b = a[::-1]
    print(f'Case #{tc}: {" ".join(b)}')