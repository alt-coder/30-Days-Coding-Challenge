def find(arr):
    start=0
    end=len(arr)-1
    while start < end:
        mid = start+((end-start)//2)
        if mid % 2 ==0:
            if(arr[mid] == arr[mid+1]):
                start=mid
            else:
                end=mid
        else:
            if(arr[mid] == arr[mid-1]):
                start=mid
            else:
                end=mid
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        if end-start <=1:
            break
    if start !=0 and arr[start]==arr[start-1]:
        return arr[end]
    else: return arr[start]

arr= [1, 3, 3, 4, 4, 5, 5, 7, 7, 8,8]
print(find(arr))