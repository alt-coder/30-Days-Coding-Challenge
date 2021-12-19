def get(arr1,arr2,m,n,k):
    if k==0 or k>m+n:
        return -1
    i=j=0
    ets=k #elements to be skiped
    newj=newi=0
    least=0
    while ets > 1:
        ets=ets//2 
        newi = i+ets if i+ets <m else m-1
        newj = j+ets if j+ets <n else n-1
        if arr1[newi] <= arr2[newj]:
            i=newi
            if i == m-1 and ets ==0 : return arr1[i]
        else:
            j= newj
            if j == n-1 and ets ==0: return arr2[j]
        #if i==m-1 or j == n-1: break
    arr=[arr2[j],arr1[i]]
    arr.sort()
    oldi=i
    oldj=j
    while i+j < k:
        if (i!=m and j!=n ) and arr1[i] < arr2[j]:
            least = arr1[i]
            i+=1
        elif (i!=m and j!=n) and arr1[i] >= arr2[j] :
            least = arr2[j]
            j+=1
        elif (i==m):
            least=arr2[j]
            j+=1
        else:
            least = arr1[i]
            i+=1
        if least not in arr:
            arr.append(least)
    return arr[k-oldi-oldj-1]
    while ets >1 :
        if i != m-1 and j!=n-1:
            if arr1[i+1]<arr2[j+1]:
                i+=1
            else:
                j+=1
            ets-=1
            continue
        else:
            break
        

    return arr1[i] if arr1[i]<arr2[j] else arr2[j]
st='''3 5 5 6 6 11 12 12 13 16 16 16 19 20 20 23 25 30 31 34 34 35 35 36 38 40 43 43 44 45 50 51 54 54 55 58 60 61 63 64 70 70 74 82 87 87 88 88 88 88 90 100'''
arr1 = [100, 112, 256, 349, 770]
arr2 = [72, 86, 113, 119, 265, 445 ,880]
arr1 = [1 ,10, 10 ,25 ,40, 54 ,79]
arr1 = list(map(int,st.split()))
arr2 = list(map(int,"15 24 27 32 33 39 48 68 82 88 90".split()))
st2="1 4 6 7 8 17 18 21 22 22 23 24 27 29 34 37 38 44 46 48 49 52 54 55 62 65 67 79 80 81 83 85 87 88 90 93 93 95 95 100"
arr2 = list(map(int,st2.split()))
print(get(arr1,arr2,len(arr1),len(arr2),4))
#some is wrong in it