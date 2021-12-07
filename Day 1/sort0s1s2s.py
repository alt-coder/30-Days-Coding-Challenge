'''
Sort an array of 0’s 1’s 2’s without using extra space or sorting algo'''

def sort012(arr):
    mp = {0:0,1:0,2:0}
    for num in arr:
        mp[num]+=1
    i=0
    while mp[0] !=0:
        num[i]=0
        i+=1
    while mp[1] !=0:
        num[i]=1
        i+=1
    while mp[2] !=0:
        num[i]=2
        i+=1
    return arr
    