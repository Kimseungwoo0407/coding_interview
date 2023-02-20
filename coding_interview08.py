# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
import collections
from typing import List


def groupAnagrams(self,strs:List[str])-> List[List[str]]:
    anagrams = collections.defaultdict(list) # 디폴트 값이 list 인 딕셔너리

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

# 참고
# {'aet': ['eat', 'tea', 'ate'], :'ant' ['tan', 'nat'], 'abt': ['bat']})