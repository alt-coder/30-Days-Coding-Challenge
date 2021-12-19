def get(arr1,arr2,m,n,k):
    if k==0 or k>m+n:
        return -1
    i=j=0
    newk=k
    newj=0
    count=0
    while newk > 1 or k-i-j-2 > 1:
        newk=newk//2 if newk !=1 else (k-i-j-2)//2
        if i == m-1 or j == n-1:
            break
        if i+newk >m-1 :
            newi = m-1
        else:
            newi=i+newk
        newj = n-1 if j+newj > n-1 else j+newk
        if arr1[newi] <= arr2[newj] :
            i=newi
        else: j=newj
    if i== m-1 or j== n-1:
        return arr2[k-m-1] if i==m-1 else  arr1[k-n-1] 
    
    if i+j+2 < k :
        if arr2[j] > arr1[i]:
            return arr2[j+1] if arr2[j+1] < arr1[i+1] else arr1[i+1]
        else:
            return arr1[i+1] if arr2[j+1] > arr1[i+1] else arr2[j+1]
    if i+j+2 ==k:
        return arr2[j] if arr2[j] > arr1[i] else arr1[i]
    else: return arr2[j] if arr2[j] <= arr1[i] else arr1[i]

    

arr1 = [100, 112, 256, 349, 770]
arr2 = [72, 86, 113, 119, 265, 445 ,880]
arr1 = [1 ,10, 10 ,25 ,40, 54 ,79]
arr2 = list(map(int,"15 24 27 32 33 39 48 68 82 88 90".split()))
print(get(arr1,arr2,len(arr1),len(arr2),15))
#some is wrong in it