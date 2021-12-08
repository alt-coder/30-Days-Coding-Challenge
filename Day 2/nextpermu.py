'''
https://leetcode.com/problems/next-permutation/
the idea is to keep on moving from right till the array is no more increasing(mark that position)

'''
def nextPermutation(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=nums[-1]
        m=-1
        for i in reversed(range(len(nums))):
            if nums[i] >= k:
                k=nums[i]
            else:
                m=i
                break
        if m != -1:                                 #if the array is not sorted in decending order
            for j in reversed(range(m+1,len(nums))): # find the element just greater than the number
                if(nums[j] > nums[m]) :              #where array is non increasing from right
                    temp = nums[m]                   #i.e number greater than that number(nums[m]) from right of array
                    nums[m] =nums[j]
                    nums[j]=temp
                    break
            n = len(nums)-1
            i=m+1
            while(i<n):                     #reverse the array from m+1 index
                temp = nums[i]
                nums[i]=nums[n]
                nums[n]=temp
                n-=1
                i+=1
            
        else:                       #if the array is in decending order reverse it
            nums.reverse()

arr=[1,3,2]
nextPermutation(arr)
print(arr)