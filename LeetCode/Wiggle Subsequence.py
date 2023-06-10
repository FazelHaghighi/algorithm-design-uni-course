class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        max_len = 1
        last_wiggle = None

        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            if (diff > 0 and last_wiggle != 1) or (diff < 0 and last_wiggle != -1):
                max_len += 1
                last_wiggle = 1 if diff > 0 else -1

        return max_len
