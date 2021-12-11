def solve(arr,target):
    ''' Methord 1 is simply iterate through the list for 2 number 
    and do two pointer technique for other 2 numbers'''
    res=set()
    arr.sort()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            left=j+1
            right = len(arr)-1
            while(left < right):
                sum=arr[i]+arr[j]+arr[left]+arr[right]
                if(sum == target):
                    res.add((i,j,left,right))
                elif sum < target:
                    left+=1
                else: right-=1
    return res

'''
The code require some improvement and need to be revisited
'''
def Methord2(arr,target):
    '''
    The worst case time complexity the program is 
    '''
    arr.sort()
    mp ={}
    res=set()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            currsum= arr[i]+arr[j]
            if target-currsum in mp:
                for item in mp[target-currsum]:
                    if type(item) != int and arr[i] not in item and arr[j] not in item:
                        res.add((arr[i],arr[j],item[0],item[1]))
            #else:
            if currsum in mp:
                mp[currsum].add((arr[i],arr[j]))
            else:
                mp[currsum]=set((arr[i],arr[j]))
    return res