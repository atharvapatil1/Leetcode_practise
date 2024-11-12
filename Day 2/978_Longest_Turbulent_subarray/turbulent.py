# We use a sliding window (l,r) to track the longest turbulent subarray, extending the window when alternating (up/down) pattern continues 
# and resetting window when pattern breaks (same direction or equal numbers).

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        res = 1
        prev = ""
        while r < len(arr):
            if arr[r-1] > arr[r] and prev != ">":
                res = max(res, r-l+1) #(if l=0,r=1, length is 2)
                r += 1
                prev = ">"
            elif arr[r-1] < arr[r] and prev != "<":
                res = max(res, r-l+1)
                r += 1
                prev = "<"
            else:
                r = r+1 if arr[r-1] == arr[r] else r
                l = r - 1
                prev = ""
        return res
        
# arr = [9,4,2,10,7,8,8,1,9]

# Initial: l=0, r=1, res=1, prev=""

# # r=1: 9,4
# arr[0] > arr[1]: (9>4)
# prev != ">" (prev is "")
# res = max(1, 1-0+1) = 2
# prev = ">"
# window = [9,4]

# # r=2: 9,4,2
# arr[1] > arr[2]: (4>2)
# prev = ">" so it's not alternating!
# l = r-1 = 1
# r = 2
# prev = ""
# window restarts at [4,2]

# # r=3: 4,2,10
# arr[2] < arr[3]: (2<10)
# prev != "<"
# res = max(2, 3-1+1) = 3
# prev = "<"
# window = [4,2,10]

# ...continues until [4,2,10,7,8,1,9]
# res = 5