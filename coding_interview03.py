import re # 정규 표현식 사용 시 내장 모듈 re 사용

## 슬라이싱을 이용한 최적화

def isPalidrome(self,s:str) -> bool:
    s = s.lower()
    
    # 정규식으로 불필요한 문자 필터링
    # re.sub('정규표현식','치환 문자','대상 문자열')
    s = re.sub('[^a-z0-9]','',s)


    return s == s[::-1] # 슬라이싱 [::-1]은 뒤집은 것

