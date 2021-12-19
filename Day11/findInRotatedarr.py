def find(arr,num):
    offset=0
    mini=arr[0]
    for i in range(1,len(arr)):
        if arr[i] < mini:
            mini= arr[i]
            offset=i
    n=len(arr)
    start=0
    end=len(arr)-1
    while(start < end):
        if(end-start) <=1:
            if arr[(end+offset)%n] == num:
                return (end+offset)%n
            end=start
        mid = start+((end-start)//2)
        actual=(mid+offset)%n
        if arr[actual] < num:
            start=mid
        elif arr[actual] > num:
            end=mid
        else:
            return actual
    return -1

arr = [3,4,5,1,2]
print(find(arr,1))