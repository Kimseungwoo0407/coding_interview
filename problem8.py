def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())