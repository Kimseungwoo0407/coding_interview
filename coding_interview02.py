import collections # namedtuple(),deque,counter 등 특수 컨테이너 데이터형 구현
from typing import Deque # 타입 어노테이션(매개 변수의 타입 명시를 위함) 사용을 위함

# 데크 자료형을 이용한 최적화


def isPalidrome(self,s:str) -> bool :
    # 데크 선언 (자료형 -> 데크형)
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1 :
        if strs.popleft() != strs.pop():
            return False
    return True
