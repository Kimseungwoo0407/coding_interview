# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

# nums = [2,7,11,15], target=9
# [0,1]

# twopointer

from typing import List

def twoSum(self,nums:List[int],target:int) -> List[int]:
    left, right = 0, len(nums)-1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left+=1
        elif nums[left] + nums[right] > target:
            right -=1
        else :
            return [left,right]