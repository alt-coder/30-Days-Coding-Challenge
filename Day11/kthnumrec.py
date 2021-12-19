def kthRec(arr1,arr2,k):
    if k==0:
        return -1
    if len(arr1) == 0:
        return arr2[k-1]
    if len(arr2) == 0 : 
        return arr1[k-1]
    if k==2:
        a=arr1[:2]+arr2[:2]
        a.sort()
        return a[1]
        #return arr2[0] if arr2[0]>arr1[0] else arr1[0]
    if k==1:
        return arr2[0] if arr2[0]<arr1[0] else arr1[0]
    if k==3:
        return kthRec(arr1[1:],arr2,k-1) if arr1[0]<=arr2[0] else kthRec(arr1,arr2[1:],k-1) 
    
    newk = k//2

    if newk >= len(arr1):
        if arr2[newk] >= arr1[-1]:
            return kthRec([],arr2,k-len(arr1))
        else:
            return kthRec(arr1,arr2[newk:],k-(newk))
    if newk >= len(arr2):
        if arr1[newk] >= arr2[-1]:
            return kthRec(arr1,[],k-len(arr2))
        else:
            return kthRec(arr1[newk:],arr2,k-(newk))
    if arr1[newk] > arr2[newk]:
        return kthRec(arr1,arr2[newk-1:],k-newk+1)
    elif arr1[newk] == arr2[newk]:
        if k%2 ==0:
            return arr1[newk-1] if arr1[newk-1]>= arr2[newk-1] else arr2[newk-1]
        else:
            return arr1[newk]
    else :
        return kthRec(arr1[newk-1:],arr2,k-newk+1)
def merge(arr1,arr2):
    i=j=0
    res=[]
    while i < len(arr1) and j < len(arr2):
        if( arr1[i] < arr2[j]):
            res.append(arr1[i])
            i+=1
        
        else:
            res.append(arr2[j])
            j+=1
    if i == len(arr1):
        return res+arr2[j:]
    else:
        return res+arr1[i:]
    
st='''3 4 5 10 14 21 26 28 28 33 34 38 39 43 49 59 64 74 84 92 96'''
arr1 = [100, 112, 256, 349, 770]
arr2 = [72, 86, 113, 119, 265, 445 ,880]
arr1 = [1 ,10, 10 ,25 ,40, 54 ,79]
arr1 = list(map(int,st.split()))
arr2 = list(map(int,"15 24 27 32 33 39 48 68 82 88 90".split()))
st2=" 5 13 15 16 16 19 19 20 20 22 23 24 32 34 34 39 41 43 46 47 49 53 58 66 67 69 70 71 72 73 73 78 80 82 83 86 87 88 90 90 91 93 93 94 96 100 100"
arr2 = list(map(int,st2.split()))
kt=merge(arr1,arr2)
print(kt[64])
print(kthRec(arr1,arr2,65))
#correct output
    