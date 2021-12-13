
def maximum1s(arr):
    i=j=-1
    mx=0
    for n,a in enumerate(arr):
        if a == 1: j=n
        else : i=n
        mx = max(mx,j-i)
    return mx

arr=[0,0,1,1,1,1,1,0,0,1,1,1]
print(maximum1s(arr))
