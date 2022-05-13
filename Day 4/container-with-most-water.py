class Solution:
    '''
    The problem require to maximize the product height (yaxis) and width(x-axis)
    In this two pointer approach we start with maximum x axis and we keep on 
    shrinking x axis in the hope of finding better or larger Y axis
    So we keep the larger point fixed and move the smaller pointer while keeping
    the track of max water '''
    def maxArea(self, nums: list[int]) -> int:
        maxwater=0
        l=0
        r=len(nums)-1
        while r > l :
            if nums[l] > nums[r]:
                maxwater = max(maxwater , nums[r] * (r-l))
                r-=1
            else:
                maxwater = max(maxwater , nums[l] * (r-l))
                l+=1
        return maxwater
'''link https://leetcode.com/problems/container-with-most-water/submissions/ '''