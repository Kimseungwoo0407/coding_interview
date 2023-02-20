## 리스트로 풀어보기!

# 주어진 문자열이 펠린드롬인지 확인
# 대소문자 구분 x, 영문자와 숫자만을 대상으로 함 -> isalnum() + lower()

# 입력 : race a car -> 출력 : false

def isPalidrome(self,s:str) -> bool :
    strs = []
    for char in s:
        if char.isalnum():
            strs.append((char.lower()))

    while len(strs) > 1 :
        if strs.pop() != strs.pop(0):
            return False

    return True
