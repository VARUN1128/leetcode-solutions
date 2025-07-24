class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = len(nums)
       
        for i in range(s+1):
            if i not in nums:
                return i
           