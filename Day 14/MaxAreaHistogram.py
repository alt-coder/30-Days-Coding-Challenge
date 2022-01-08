def nextSmallRight(arr):
    ls=[]
    ans=[-1]*len(arr)
    for i,num in enumerate(arr):
        if not ls or arr[ls[-1]] <= num:
            ls.append(i)
        else:
            while(ls and arr[ls[-1]] > num):
                ans[ls.pop()] = i
            ls.append(i)
    return ans

def nextSmallLeft(arr):
    ls=[]
    arr2=list(reversed(arr))
    print(arr2)
    n=len(arr)
    ans=[-1]*len(arr)
    for i,num in enumerate(arr2):
        if not ls or arr2[ls[-1]] <= num:
            ls.append(i)
        else:
            while(ls and arr2[ls[-1]] > num):
                ans[ls.pop()] = i
            ls.append(i)
    for i in range(n):
        if ans[i] !=-1 :
            ans[i]=n-1-ans[i]
    return ans

def RectagleArea(arr):
    right = nextSmallRight(arr)
    left = nextSmallLeft(arr)
    left.reverse()
    area=0
    w=[0]*len(arr)
    for i in range(len(arr)):
        l = 0 if left[i] == -1 else left[i]
        r= 0 if right[i] == -1 else right[i]
        w[i] = abs(r-l)+1
        ht=0
        w[i]=abs(left[i]-right[i])-1    
        area = max(area,w[i]*arr[i])
    return area

arr=[2,1,6,5,6,2,3]
print(RectagleArea(arr))