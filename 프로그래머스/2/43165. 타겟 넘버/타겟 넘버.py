def solution(numbers, target):
    answer = 0
    # 모든 경우를 세야하니까, DFS. 재귀쓰는거.
    
    def dfs(index, total):
        nonlocal answer
        
        if index == len(numbers):
            if total == target:
                answer += 1
                
            return
            
        # +하는경우
        dfs(index+1, total+numbers[index])
        
        # -하는 경우
        dfs(index+1, total-numbers[index])
        
    dfs(0,0)
    

    return answer