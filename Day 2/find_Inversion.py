'''
Minimum number of moves for an arry to be sorted
utilize merge proceduce
[2,3,1] #(i ,j are pointers)
[2,3](i=0) and [1](j=0) to be  merge
2>1 => 3>1
at lease two moves are req = len(a1)-j

'''
def merge(arr1,arr2,ct):
    if arr1 is None:
        return arr2
    if arr2 is None:
        return arr1
    res = []
    i=j=0
    while(i< len(arr1) or j <len(arr2)):
        if i>= len(arr1):
            res.append(arr2[j])
            j+=1
        elif j >= len(arr2):
            res.append(arr1[i])
            i+=1
        elif arr1[i] < arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            ct[0] += (len(arr1)-i)
            res.append(arr2[j])     #a2[j] > a1[j] so calulate count
            j+=1
    return res

def mergesort(arr,ct):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) //2
    r=merge(mergesort(arr[:mid],ct),mergesort(arr[mid:],ct),ct)
    #print(ct)
    return r

def countinversion(arr):
    ct=[0]
    mergesort(arr,ct)
    return ct[0]

print(countinversion([8,4,2,1]))
