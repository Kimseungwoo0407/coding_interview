# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

# nums = [2,7,11,15], target=9
# [0,1]

# 딕셔너리를 이용

from typing import List


def twoSum(self,nums:List[int],target:int) -> List[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
    
    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i , num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target-num]:
            return [i, nums_map[target-num]]