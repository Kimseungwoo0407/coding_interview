import collections # Counter, defaultdict, deque 등이 쓰임

def isPalindrome(self, s:str) -> bool:
    # 자료형 데크로 선언 (strs)
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum(): # isalnum을 통해 문자와 숫자만 남김
            strs.append(char.lower()) # 소문자로 바꾼 뒤 strs에 추가

    while len(strs) > 1:
        if strs.popleft() != strs.pop(): # 맨 앞부분과 맨 뒷부분 추출 후 비교
            return False
    
    return True