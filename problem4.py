# 문자열 뒤집는 함수 작성

str = ['h','e','l','l','o']

def reversestr(self, s:list[str]) -> None :
    left, right = 0, len(s) -1
    while left < right :
        s[left], s[right] = s[right],s[left]
        left+=1
        right-=1
    print(s)

reversestr(str,str)