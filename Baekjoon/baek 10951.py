import sys
lines = sys.stdin.realines()
for line in lines:
    A, B = map(int, line.split())
    print(A+B)