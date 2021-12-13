
def tapping(arr):
    mx = arr[0]
    aux1=[]
    for i in  arr:
        aux1.append(max(i,mx))
        mx=max(mx,i)
    mx = arr[-1]
    aux2 = []
    for j in reversed(arr):
        aux2.append(max(j,mx))
        mx=max(mx,j)
    aux2.reverse()
    sum = 0
    for i in range(len(arr)):
        sum += min(aux1[i],aux2[i]) - arr[i]
    return sum

def M2(arr):
    L=1
    R=len(arr)-2
    maxL=arr[0]
    maxR = arr[-1]
    sum=0
    while(L <= R):
        if maxL <= maxR:
            if arr[L] <= maxL:
                sum+= maxL-arr[L]
                
            else:
                maxL = arr[L]
            L+=1
        else:
            if arr[R] <= maxR:
                sum+= maxR-arr[R]
                
            else:
                maxR = arr[R]
            
            R-=1
    return sum



arr = [3,1,2,4,0,1,3,2]

print(M2(arr))