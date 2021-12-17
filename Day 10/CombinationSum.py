comb=[]
def CombinationSum(num,target,current,ans,j):
    global comb
    if current == target:
        ans.append(comb)
        # comb=[]
        return
    if current > target:
        return
    for i in range(j,len(num)):
        if current+num[i] <= target:
            comb.append(num[i])
            #current=
            CombinationSum(num,target,current+num[i],ans,i)
            
            comb=comb[:-1]
        else:
            return
        


ans=[]


arr=[2,7,6,3,5,1]

target=9
current=0
arr.sort()
CombinationSum(arr,target,current,ans,0)
print(ans)
candidates=[]
path=[]
def dfs(start, curSum):  
            if curSum == target: 
                ans.append(path[:])
                return 

            for i in range(start, len(candidates)): 
                if curSum + candidates[i] > target: 
                    break 
                    
                path.append(candidates[i])
                dfs(i, curSum + candidates[i])
                path.pop()
        
def solve():        
    candidates.sort()
    ans, path = [], []
    dfs(0, 0)
    return ans 