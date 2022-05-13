class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) > 0:
            maxsum=nums[0]   ##the first value as maximum value
            cursum=0
        else:
            maxsum=0
        for num in nums:
            cursum+=num
            if cursum <num:  # by adding a number , if the current sum gets less than that number 
                cursum=num   #then no use of old cursum , make current sum as that number
            maxsum = max(cursum,maxsum)
            
        return maxsum