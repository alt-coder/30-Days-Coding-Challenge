class Solution:
    def __init__(self):
        self.ans=[]
        self.current=[]
    def ispalindrome(self,s,start,end):
        while start<=end and end>=0:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1
        return True
    def substr_start(self,s,start):
        '''all substring function based on startindex'''
        if (start==len(s)):
            self.ans.append(self.current)
            return

        for i in range(start,len(s)):
            # print(s[start:i+1])
            if self.ispalindrome(s,start,i):
                self.current.append(s[start:i+1])
                self.substr_start(s,i+1)
                self.current= self.current[:-1]
                # print(s[start:i+1])
ob=Solution()
#print(ob.ispalindrome("ab",1,1))
ob.substr_start("abaaba",0)
print(ob.ans)