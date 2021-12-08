
def solve(arr):
    maxprofit =0
    minnum= float("inf")
    for i in range(len(arr)):
        if arr[i] < minnum:
            minnum = arr[i]
        maxprofit = max(arr[i]-minnum,maxprofit)
    return maxprofit
print(solve([7,6,4,3,1]))