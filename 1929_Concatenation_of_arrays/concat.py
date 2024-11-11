# Method 1: Using Stack
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        stack = []
        for i in range(2):
            for j in nums:
                stack.append(j)
        return stack
    
# Method 2: Using extend function in python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums