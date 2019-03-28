import collections

def solution(participant , completion):
    col = collections.Counter(participant)
    col2 = collections.Counter(completion)

    result = col - col2
    answer = list(result.keys())[0]
    return answer
