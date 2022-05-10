class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l=len(nums)
        ans = [1]*l #define answer array
        pre=suf=1 #define current prefix product and suffix product
        
        for i in range(l):
            ans[i] *= pre
            pre*=nums[i]
            ans[l-1-i]*=suf
            suf *= nums[l-1-i]
        return ans
'''https://leetcode.com/problems/product-of-array-except-self'''