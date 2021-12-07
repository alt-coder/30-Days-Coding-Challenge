def findmaxcontinuous(arr):
    maxsofar=currmax=0
    start=end=0
    for i,a in enumerate(arr):
        currmax +=a
        if currmax < 0:
            currmax = 0
            start=end=i+1
        maxsofar = max(maxsofar,currmax)
        if maxsofar == currmax : end =i
    return maxsofar