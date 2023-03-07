# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
# nums = [-1,0,1,2,-1,-4]

from typing import List

def threeSum(self, nums:List[int])-> List[int]:
    results=[]
    nums.sort()

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # 간격 좁혀가며 합 sum 계산
        left,right= i+1, len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0 :
                left+=1
            elif sum > 0 :
                right -= 1
            else:
                # sum = 0인 경우이므로 정답 및 스킵 처리
                results.append([nums[i],nums[left],nums[right]])
                
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return results
