import math
test_case = int(input())

for _ in range(test_case):
    answer = 0
    x1, y1, r1, x2, y2, r2= map(int, input().split())

    dx, dy = abs(x1-x2), abs(y1-y2)
    dist = dx**2 + dy**2
    r_sum = (r1+r2)**2
    r_diff = (r1-r2)**2

    if dist == 0 and r1 == r2:
        print(-1)

    elif dist == r_sum or dist == r_diff:
        print(1)

    elif r_diff < dist < r_sum:
        print(2)

    else:
        print(0)
