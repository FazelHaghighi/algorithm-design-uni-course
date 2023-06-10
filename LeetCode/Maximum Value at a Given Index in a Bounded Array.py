import math

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n  # remove the contributions from all the 1 in each element
        # We will add 1 back to the final height later
        
        if index < n // 2:
            index = n - index - 1
        n_left = index
        n_right = n - 1 - index
        
        tri_left = (n_left * (n_left + 1)) // 2
        tri_right = (n_right * (n_right + 1)) // 2
        
        # Case 1: perfect pyramid
        if maxSum <= (tri_right * 2 + n_right + 1):
            return int(math.sqrt(maxSum)) + 1
        
        # Case 2: right side hits the boundary
        if maxSum <= (tri_left + tri_right + (n_left - n_right) * n_right + n_left + 1):
            b = 3 + 2 * n_right
            return int((-b + math.sqrt(b * b - 8 * (tri_right + 1 - n_right * n_right - maxSum))) / 2) + 1 + 1
        
        # Case 3: both sides hit boundaries
        maxSum -= (tri_left + tri_right + (n_left - n_right) * n_right + n_left + 1)
        return n_left + 1 + 1 + (maxSum // n)
