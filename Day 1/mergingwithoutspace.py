'''
maintain three pointer i j k=n-1 such that (n=len(arr1))
if at any point an element in a2 is less than a element in arr1 then that element at a2 must be at arr 1
if a1[i] < a2[j]:
    i++
else :
    swap(a2[j],a1[k])
    j++,k--
'''

def merge(a1,a2):
    i=j=0
    k= len(a1)-1
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            i+=1
        else:
            temp = a2[j]
            a2[j]  =a1[k]
            a1[k] = temp
            j+=1
            k-=1
    a1.sort()
    a2.sort()
    return

arr1 = [1,3,7,12,20]
arr2 = [2,5,6,10,11,19]

merge(arr1,arr2)
print(arr1,arr2)
