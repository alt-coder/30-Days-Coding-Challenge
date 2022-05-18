#Monotonic Stack
class Solution:
 
    def dailyTemperatures(self, temp: list[int]) -> list[int]:
        stack=[(temp[0],0)]
        ans=[0]*len(temp)
        for i,e in enumerate(temp[1:]):
            
            while len(stack)>0 and stack[-1][0]<e:
                top = stack.pop()
                ans[top[1]]=i+1-top[1]
            stack.append((e,i+1))
        
        return ans

##explanation available in one note 