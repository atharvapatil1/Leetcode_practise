class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        maxsum = nums[0]
        L = 0
        for R in range(len(nums)):
            cursum = max(cursum,0) + nums[R]
            maxsum = max(maxsum, cursum)
        return maxsum
    
# nums = [-2, 3, -1, 4]

# # R = 0, nums[0] = -2
# cursum = max(0,0) + (-2) = -2
# maxsum = max(-2, -2) = -2

# # R = 1, nums[1] = 3
# cursum = max(-2,0) + 3 = 3   # Reset negative sum to 0, then add 3
# maxsum = max(-2, 3) = 3

# # R = 2, nums[2] = -1
# cursum = max(3,0) + (-1) = 2  # Keep positive sum 3, then add -1
# maxsum = max(3, 2) = 3

# # R = 3, nums[3] = 4
# cursum = max(2,0) + 4 = 6
# maxsum = max(3, 6) = 6