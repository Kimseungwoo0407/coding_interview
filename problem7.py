# 가장흔한단어

def mostCommonWord(self, paragraph: str, banned: list[str]) -> str :
    words = [word for word in re.sub(r'[^\w]',' ', paragraph) # 단어 문자가 아닌 모든 문자를 공백으로 치환
            .lower().split()
            if word not in banned]
    counts = collections.Counter(words)

    # 가장 흔하게 등장하는 단어의 첫번째 인덱스 리턴
    return counts.most_common(1)[0][0]