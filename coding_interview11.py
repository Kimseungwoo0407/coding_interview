# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

# nums = [2,7,11,15], target=9
# [0,1]

# in을 이용

from typing import List


def twoSum(self,nums:List[int],target:int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target-n
        
        if complement in nums[i+1:]:
            return [nums.index(n),nums[i+1:].index(complement)+(i+1)]

