# 문자열 뒤집는 함수 작성

def reversestr(self, s:list[str]) -> None :
    left, right = 0, len(s) -1 # 0부터 세기에 각각 0, len(s) -1 값을 넣어준다.
    while left < right : # 둘이 가로지를 때 그만
        s[left], s[right] = s[right],s[left] # left에 right, right에 left를 통해 반대값을 줌
        left+=1 # 1씩 증가
        right-=1 # 1씩 감소
