# Use 2 pointer method left and right, where right will traverse from 1 to len
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1                                      # Position where next unique element should be placed
        for right in range(1, len(nums)):            # Iterate through array starting from second element
            if nums[right] != nums[right-1]:         # If current element is different from previous element
                nums[left] = nums[right]             # Place the unique element at left pointer
                left += 1                            # Move left pointer to next position
        return left                                  # Return the length of array with unique elements

# nums = [1,1,2,2,3]

# Initial state: 
# - left = 1
# - The array remains [1,1,2,2,3]

# First iteration (right = 1):
# - nums[1] == nums[0] (1 == 1)
# - No action needed as it's a duplicate

# Second iteration (right = 2):
# - nums[2] != nums[1] (2 != 1)
# - Place 2 at left (index 1)
# - left becomes 2
# - Array becomes [1,2,2,2,3]

# Third iteration (right = 3):
# - nums[3] == nums[2] (2 == 2)
# - No action needed as it's a duplicate

# Fourth iteration (right = 4):
# - nums[4] != nums[3] (3 != 2)
# - Place 3 at left (index 2)
# - left becomes 3
# - Array becomes [1,2,3,2,3]

# Final result:
# - Returns left = 3
# - First three elements are unique: [1,2,3,...]