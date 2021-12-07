 '''
 Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 '''
 
 
 
def findDuplicate(self, nums) -> int:
        ''' We can utilize the fact the numbers
        the number are in range of [1,n]
        approach:
        use the array itself to know the repeated elemen if two idx map to same number
        return that index
        use index as function of nums
        
        '''
        sum =0
        for i in range(len(nums)): 
            idx = abs(nums[i])
            if (nums[idx] < 0):
                return idx
            nums[idx] *= -1
        
        