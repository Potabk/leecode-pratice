from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = []
        for q in range(2):
            for i in range(len(nums)):
                while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                    result[stack[-1]] = nums[i]
                    stack.pop()
                    stack.append(i)
        return result


