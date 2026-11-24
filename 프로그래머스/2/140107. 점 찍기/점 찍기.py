import math
def solution(k, d):
    x = 0
    a = 0
    answer = 0
    
    while x <= d:
        max_y = math.sqrt(d**2-x**2)
        a = max_y // k
        answer += (a +1)
        x += k
    
    return answer
    