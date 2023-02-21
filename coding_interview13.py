# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

# nums = [2,7,11,15], target=9
# [0,1]

# 하나의 for 문

from typing import List


def twoSum(self,nums:List[int],target:int) -> List[int]:
    nums_map = {}
    # 하나의 for 문으로 통합
    for i , num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num],i]
        nums_map[num] = i