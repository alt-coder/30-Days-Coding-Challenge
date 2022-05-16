class Solution:
    def gen(self,o,c,ans,st):
        '''
        o= number of open brackets that can be added to the string
        c = "........"closed"..................................."
        ans= array to hold the resultant string
        st='string that has been formed till now'
        '''
        #base case when we have balanced brackets
        if o ==0 and c == 0 :
            ans.append(st)
        elif o==c:      # case when we have balanced brackets but less than n
            st+='('
            self.gen(o-1,c,ans,st)
        if o<c and o >= 0:  # case when open are more than closed and open less than n
            b=str(st)
            st+='('
            self.gen(o-1,c,ans,st)
            b+=')'
            self.gen(o,c-1,ans,b)
            
        
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        self.gen(n-1,n,ans,'(') #all string must start from open bracket
        return ans
        