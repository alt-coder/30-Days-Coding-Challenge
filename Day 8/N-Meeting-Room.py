
def NMeeting(start,end):
    arr = [(i,j) for i,j in zip(start,end)]
    arr.sort(key= lambda x: x[1])
    ans=[arr[0]]
    for item in arr[1:]:
        if item[0] > ans[-1][0]:
            ans.append(item)
    return len(ans)

print(NMeeting([1,3,0,5,8,5],[2,4,6,7,9,9]))