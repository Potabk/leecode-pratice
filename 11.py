class Solution:
    def maxArea(self, height: List[int]) -> int:
        res =0
        i = 0
        j = len(height)-1
        while i<j:
            if  height[i] < height[j]:
                res = max(res, height[i]*(j - i))
                i+= 1
            else:
                res = max(res, height[i]*(j-i))
                j-= 1
        return res
