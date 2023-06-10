class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        start, end = 0, 0
        
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)  # Check for odd-length palindromes
            len2 = self.expandAroundCenter(s, i, i + 1)  # Check for even-length palindromes
            length = max(len1, len2)
            
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        
        return s[start:end+1]
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - left - 1
