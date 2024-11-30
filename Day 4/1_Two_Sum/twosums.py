class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in hashMap:
                return [hashMap[diff],i]
            hashMap[nums[i]] = i
        return []

# nums = [3,2,4], target = 6

# # i = 0, nums[0] = 3
# diff = 6 - 3 = 3
# hashMap = {}
# 3 not in hashMap
# Add to hashMap: {3: 0}

# # i = 1, nums[1] = 2
# diff = 6 - 2 = 4
# 4 not in hashMap
# Add to hashMap: {3: 0, 2: 1}

# # i = 2, nums[2] = 4
# diff = 6 - 4 = 2
# 2 is in hashMap! ✓
# return [hashMap[2], 2] = [1, 2]