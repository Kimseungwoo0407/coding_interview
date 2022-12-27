def isPalindrome(self,s: str) -> bool: # 타입 힌트로 리턴 값이 True or False인 것을 알 수 있다.
        strs = [] # 빈 문자열 선언
        for char in s: 
            if char.isalnum(): # char.isalnum()은 영문자, 숫자 여부를 판별하는 함수, 해당하는 문자만 추가
                strs.append(char.lower()) # 문제에서 대소문자를 구분하지 않으므로 lower()로 모두 소문자로 변환

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop(): # strs.pop(0)을 통해 strs의 첫번째 요소를 가져오고 strs.pop()으로 마지막 요소를 가져와 일치 True, 불일치 False
                return False

        return True

