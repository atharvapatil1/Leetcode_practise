# Method 1: Using stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack or \
                (c == ")" and stack[-1] != "(") or \
                (c == "]" and stack[-1] != "[") or \
                (c == "}" and stack[-1] != "{"):
                    return False
                stack.pop()
        return not stack 
# If stack is empty ([]), "not stack" evaluates to True, meaning all brackets were properly closed
# If stack still has items, "not stack" evaluates to False, meaning some opening brackets were never closed

# Method 2: Using Hashmap
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoOpen = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in closetoOpen: #if closing parenthesis occured first
                if stack and stack[-1] == closetoOpen[c]: # stack: First checks if the stack is not empty, stack[-1] == closetoOpen[c]: Then checks if the most recent opening bracket matches
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)
        return True if not stack else False #not stack means empty?