class Solution(object):
    def canJump(self, nums):
        curr = nums[0]
        for i in range(1, len(nums)):
            if curr == 0:
                return False
            curr -= 1
            curr = max(curr, nums[i])
        return True
