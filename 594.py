# 最长和谐子序列
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        my_dict = {}
        for i in nums:
            dict[i] = my_dict.get(i,0) + 1
        for i in my_dict:
            if i+1 in my_dict:
                res = max(res, my_dict[i] + my_dict[i+1])
        return res
