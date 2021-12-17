


class Solution:
    def __init__(self):
        self.path=[]
        self.ans=[]
        self.start=0
        self.current=0
    ans,path=[],[]
    target=0
    def CSum(self,candidates,start,target):
        if self.current == target:
            self.ans.append(self.path)
            return
        for i in range(start,len(candidates)):
            if i>start and candidates[i-1]==candidates[i]: continue
            if self.current+candidates[i] > target:
                break
            self.current+=candidates[i]
            self.path.append(candidates[i])
            
            self.CSum(candidates,i+1,target)
           
            self.current-=candidates[i]
            self.path=self.path[:-1]
        return
    def combinationSum2(self,candidates,target):
        self.path=[]
        self.ans=[]
        self.start=0
        self.current=0
        candidates.sort()
        self.CSum(candidates,0,target)
        # print(set(self.ans))
        return self.ans
        
sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5],8))