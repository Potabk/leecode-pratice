class Solution:
    def isPalindrome(self, x: int) -> bool:
        return (s :=str(x)) == s[::-1] and x>=0