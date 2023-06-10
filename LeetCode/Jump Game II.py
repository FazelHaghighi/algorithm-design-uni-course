from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        jumps = 0
        current_max_reach = nums[0]
        next_max_reach = nums[0]

        for i in range(1, len(nums)):
            if i > current_max_reach:
                jumps += 1
                current_max_reach = next_max_reach

            next_max_reach = max(next_max_reach, i + nums[i])

        return jumps + 1
