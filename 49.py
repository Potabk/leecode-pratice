from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for str in strs:
            hashmap[''.join(sorted(str))].append(str)
        return list(hashmap.values())


if __name__ == '__main__':
    s = Solution()
    res = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(res)
