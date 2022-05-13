def threeSum(nums: list[int]) -> list[list[int]]:
        target=0
        nums.sort()
        ans=[[1,8,9]]
        i=0
        while i <len(nums)-2:
            while i>0 and i <len(nums)-2 and nums[i] == nums[i-1] : i+=1
            l=i+1
            r=len(nums)-1
            # while l < r-1 and nums[l] == nums[l+1] : l+=1
            num=nums[i]
            while l<r:
                if(nums[l]+nums[r]+num==target):
                    # if not (ans[-1][0] == num and ans[-1][1] == nums[l] and ans[-1][2] == nums[r]) :
                    ans.append([num,nums[l],nums[r]])
                    r-=1
                    while l<r and nums[r] == nums[r+1] :
                        r-=1
                elif(nums[l]+nums[r]+num > target) : r-=1
                else: l+=1
            i+=1
        return ans[1:]

print(threeSum([-1,0,1,0]))

### Wrong Submission
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        target=0
        nums.sort()
        ans=[[1,8,9]]
        i=0
        while i <len(nums)-2:
            while i>0 and i <len(nums)-2 and nums[i] == nums[i-1] : i+=1 
            ''' mistake: skipping the initial repeation
            and considering the last repeated
            does not allow for nums[l] to be same as num[i] for example [3,5,5,5[i],6[l],6,7[r]] is wrong as one possiblity
            could be [3,5[i],5[l],5,6,6,7[r]]'''
            l=i+1
            r=len(nums)-1
            # while l < r-1 and nums[l] == nums[l+1] : l+=1
            num=nums[i]
            while l<r:
                if(nums[l]+nums[r]+num==target):
                    # if not (ans[-1][0] == num and ans[-1][1] == nums[l] and ans[-1][2] == nums[r]) : # this wont work 
                    ans.append([num,nums[l],nums[r]])
                    l+=1 # mistake 2 
                    '''
                    if we increment l then num[l+1] can be equal to num[l] and we may get repitition on the ans
                    so either increment l in such a way that new value of l different or 
                    decrement r untill r has a different value.
                    r-=1 would fix the code if we follow the next code line(decrement of r)
                    '''
                    while l<r and nums[r] == nums[r-1] : r-=1
                elif(nums[l]+nums[r]+num > target) : r-=1
                else: l+=1
            i+=1
        return ans[1:]
            