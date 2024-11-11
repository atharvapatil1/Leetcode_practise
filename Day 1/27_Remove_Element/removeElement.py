class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0                                     # Position to place elements that are not equal to val
        for right in range(0, len(nums)):           # Iterate through each element in the array
            if val != nums[right]:                  # If current element is not equal to val
                nums[left] = nums[right]            # Place it at the left pointer position
                left += 1                           # Move left pointer to next position
        return left                                 # Return count of elements not equal to val
    
# nums = [3,2,2,3], val = 3

# Initial state:
# - left = 0
# - Array is [3,2,2,3]

# First iteration (right = 0):
# - nums[0] = 3 equals val
# - Skip as we want to remove it

# Second iteration (right = 1):
# - nums[1] = 2 doesn't equal val
# - Place 2 at left (index 0)
# - left becomes 1
# - Array becomes [2,2,2,3]

# Third iteration (right = 2):
# - nums[2] = 2 doesn't equal val
# - Place 2 at left (index 1)
# - left becomes 2
# - Array becomes [2,2,2,3]

# Fourth iteration (right = 3):
# - nums[3] = 3 equals val
# - Skip as we want to remove it

# Final result:
# - Returns left = 2
# - First two elements are not equal to val: [2,2,...]