
def solution(arr):
    i=0
    j=1
    n= len(arr)
    res=[arr[0]]
    for i in arr[1:]:
        if res[-1] != i:
            res.append(i)
    return res

def sol2(arr):
    i=0
    j=1
    n= len(arr)
    ct=0
    while j < n:
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i+=1
        j+=1
    return arr[:i+1]


arr=[1,1,1,2,2,2,3,3,4]
print(solution(arr))
print(sol2(arr))
