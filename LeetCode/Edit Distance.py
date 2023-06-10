class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        return self.helper(word1, word2, 0, 0, memo)
    
    def helper(self, word1: str, word2: str, i: int, j: int, memo: dict) -> int:
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if word1[i] == word2[j]:
            result = self.helper(word1, word2, i + 1, j + 1, memo)
        else:
            insert = 1 + self.helper(word1, word2, i, j + 1, memo)
            delete = 1 + self.helper(word1, word2, i + 1, j, memo)
            replace = 1 + self.helper(word1, word2, i + 1, j + 1, memo)
            result = min(insert, delete, replace)
        
        memo[(i, j)] = result
        return result
