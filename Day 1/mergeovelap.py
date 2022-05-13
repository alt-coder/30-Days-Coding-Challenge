def meroverlap(arr):
    if len(arr) == 0:
        return arr
    st = sorted(arr,key= lambda x:(x[0],-x[1])) #sort the interval and incase of tie make sure large end interval come first
    ans =[]
    ans.append(st.pop(0))       #append the first element as it is
    while st:
        if ans[-1][1] >= st[0][0]:      #if last element end is >= sorted list start
            ans[-1][1] = max(st[0][1],ans[-1][1])   #merge them
        else :
            ans.append(st.pop(0))       #else append the interval as it is
    return ans

def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key= lambda x :x[0]) #sort the interval as per start time
        ans=[intervals[0]]
        for num in intervals[1:]:
            if(num[0]<=ans[-1][1]):  #condition of being merged
                ans[-1][1]=max(num[1],ans[-1][1]) #only the last end time needs to be updated after merging
            else: ans.append(num)
        return ans

# no extra space
def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key= lambda x :x[0])
    i=0
    for num in intervals[1:]:
        if(num[0]<=intervals[i][1]):
            intervals[i][1]=max(num[1],intervals[i][1])
        else:
            i+=1
            intervals[i]=num
    return intervals[:i+1]
    