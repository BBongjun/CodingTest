n_test = int(input())

def answer():
    x_start, y_start, x_end, y_end = map(int, input().split())
    n_meet = 0

    n_planet = int(input())
    for _ in range(n_planet):
        x_planet, y_planet, r_planet = map(int, input().split())

        # start와 관계
        d_start = (x_start - x_planet)**2 + (y_start - y_planet)**2
        d_end = (x_end - x_planet)**2 + (y_end - y_planet)**2

        is_in_start = d_start < r_planet**2
        is_in_end = d_end < r_planet**2

        if is_in_start != is_in_end:
            n_meet+=1

    print(n_meet)


for _ in range(n_test):
    answer()
