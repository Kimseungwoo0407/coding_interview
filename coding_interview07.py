# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자 구분 하지 않으며, 구두점 또한 무시한다.
import collections
import re
from typing import List

def mostCommonWord(self, paragraph:str,banned:List[str]) -> str:
    
    # re.sub(r'[^\w]','',paragraph) -> 단어 문자가 아닌것은 공백 치환
    words = [word for word in re.sub(r'[^\w]','',paragraph).lower().split()
    if word not in banned]

    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    return counts.most_common(1)[0][0]


# 참고
# from collections import Counter
# Counter(["hi", "hey", "hi", "hi", "hello", "hey"]) -> Counter({'hi': 3, 'hey': 2, 'hello': 1})