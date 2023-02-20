# 로그를 재정렬하기
# 1. 로그의 가장 앞 부분은 식별자
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다 -> 문자와 숫자 로그를 구분
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.
from typing import List


def reorderLogFiles(self, logs: List[str]) -> List[str] :
    letters, digits = [], [] # 구분
    for log in logs:
        if log.split()[1].isdigit(): # 숫자로 변환 가능한 로그 확인
                                     # log.split()[0]은 식별자 이므로 [1]을 확인
            digits.append(log)
        else:
            letters.append(log)
    #     
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

# 참고 (log.split()할 시 이렇게 됨)
# ['dig1', '8', '1', '5', '1']
# ['let1', 'art', 'can']
# ['dig2', '3', '6']
# ['let2', 'own', 'kit', 'dig']
# ['let3', 'art', 'zero']