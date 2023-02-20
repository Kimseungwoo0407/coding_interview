# 문자열 뒤집는 함수 작성, 입력 값은 문자 배열, 리턴 없이 리스트 내부 직접 조작
# 투 포인터를 이용한 스왑
from typing import List

def reverseString(self,s :List[str]) -> None :
    left, right = 0, len(s) -1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left+=1
        right-=1
