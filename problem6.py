logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6','let2 own kit dig','let3 art zero']

def reorderLogFiles(self, logs:list[str]) -> list[str] :
    letters, digits = [], []
    for log in logs :
        if log.split()[1].isdigit(): # is.digit()을 통해 숫자 여부 확인
            digits.append(log) # 숫자 변환 가능한 로그는 digits
        else:
            letters.append(log) # 그렇지 않은 문자 로그는 letters

    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) # 식별자를 제외한 문자열 [1:]을 키로하여 정렬, 동일한 경우 후순위로 식별자 [0]를 지정해 정렬
    return letters + digits


