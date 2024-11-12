class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax = globMin = nums[0]
        total = curmax = curmin = 0
        for n in nums:
            curmax = max(curmax + n, n)
            curmin = min(curmin + n, n)
            globMax = max(globMax, curmax)
            globMin = min(globMin, curmin)
            total += n
        return max(globMax, total-globMin) if globMax > 0 else globMax  #This handle third case of input example

# This algorithm finds both the maximum regular subarray (globMax) and maximum wrapped subarray (total-globMin) 
# and chooses the larger one, but for all-negative arrays it returns the largest negative number since wrapping won't help.

# Case 1: [5,-3,4] # Max sum is regular (no wrapping)
# # n = 5
# curmax = max(0+5, 5) = 5
# curmin = min(0+5, 5) = 5
# globMax = 5, globMin = 5, total = 5

# # n = -3
# curmax = max(5-3, -3) = 2
# curmin = min(5-3, -3) = -3
# globMax = 5, globMin = -3, total = 2

# # n = 4
# curmax = max(2+4, 4) = 6
# curmin = min(-3+4, 4) = 1
# globMax = 6, globMin = -3, total = 6

# Final: max(globMax=6, total-globMin=6-(-3)=9)
# Returns 9 (wrap around: 4,5)

# Case 2: [-3,-2,-1] # All negative 
# # n = -3
# curmax = max(0-3, -3) = -3
# curmin = min(0-3, -3) = -3
# globMax = -3, globMin = -3, total = -3

# # n = -2
# curmax = max(-5, -2) = -2
# curmin = min(-5, -2) = -5
# globMax = -2, globMin = -5, total = -5

# # n = -1
# curmax = max(-3, -1) = -1
# curmin = min(-6, -1) = -6
# globMax = -1, globMin = -6, total = -6

# Since globMax < 0, return globMax = -1

