# from collections import Counter

# def solution(citations):
#     answer = 0
#     citations.sort(reverse=True)
#     for possible_h in range(len(citations),-1,-1):
#         new_cite = list(map(lambda x : int(x >= possible_h), citations))
#         if Counter(new_cite)[1] >=possible_h:
#             answer = possible_h
#             break

#     return answer

# def solution(citations):
#     citations.sort(reverse=True)
#     answer = len(citations)
#     for i, citation in enumerate(citations):
#         if citation <= i:
#             answer = i
#             break
#     return answer



def solution(citations):
    answer=0
    citations.sort(reverse=True)
    
    for i, citation in enumerate(citations):
        h = i+1
        if citation >= h:
            answer = h
    return answer
            
    

















