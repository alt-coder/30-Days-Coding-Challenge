def solve(arr):
    '''
    if sum is ever repeated in that array it means that ans is equal to the
    difference of current sum index and  previous sum index
    '''
    mp={arr[0]:0}
    ans=0
    sum=arr[0]
    for i in range(1,len(arr)):
        sum +=arr[i]
        if sum in mp:
            ans= max(ans,i-mp[sum])
        else:
            mp[sum]=i
    return ans

print(solve([15, -2, 2, -8, 1, 7, 10, 23]))
print(solve([1,0,3]))