class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ""
        for c in s:
            if c.isalnum():
                alpha += c.lower()
        return True if alpha[:] == alpha[::-1] else False

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))