def nextLargerElement(self,arr,n):
        #code here
        ls=[]
        mp={}
        for element in arr:
            if len(ls)==0:
                ls.append(element)
                continue
            if element > ls[-1]:
                #ans.append(element)
                while len(ls)!=0 and element > ls[-1]  :
                    mp[ls.pop()]=element
            ls.append(element)
        ans=[mp[element] if element in mp else -1 for element in arr]
        # for element in arr:
        #     if element in mp:
        #         ans.append(mp[element])
        #     else:
        #         ans.append(-1)
        return ans

arr= [1,3,2,4]
print(nextLargerElement(1,arr,len(arr)))