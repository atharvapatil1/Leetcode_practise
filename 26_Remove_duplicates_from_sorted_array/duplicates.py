# Use 2 pointer method left and right, where right will traverse from 1 to len
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1                                      # Position where next unique element should be placed
        for right in range(1, len(nums)):            # Iterate through array starting from second element
            if nums[right] != nums[right-1]:         # If current element is different from previous element
                nums[left] = nums[right]             # Place the unique element at left pointer
                left += 1                            # Move left pointer to next position
        return left                                  # Return the length of array with unique elements