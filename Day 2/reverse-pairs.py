#intuition 
'''
array = [3,1]
3 > 1*2
so answer is one 
therefore the number(1) in the right will always be less than the number on the left(3)
So if we sort the array then simiply we need to calculate the count of numbers(in the array)
 which are greater than 2 times of the number on the right from the its(right number)
  sorted position to its current position. 
in merge sort we can see it 

example   [2,4,3, 5,1]
        /             \
       /               \
    [2,4,3]             [5,1]    
    /       \       /   \
    [2,4]   [3]   [5]    [1]    0 <- swaps
    
    [2,4,3] 1 swap but 4 is not > 3*2     [5,1]   1swap    [1,5] also 5 is greater than 2*1 
    
    next step 
     [5]   [1] will give [1,5] after adding right[1] in left[5]
     
     so we need to check how many number in left could form a reverse pair with 1
     since we have one number(5) so we can check eaisly
     5 > 2*1 so we have one pair
     
     More clearly in later step we can see
    
    [2,3,4]             [1,5] till now one valid reverse pair [5 and 1]
    from this step, 1 had to come to first position of left array from its
     current position at 4(first of right arr)
    so from second position [i.e from 2,3,4] we keep on checking whether any number > 2*1
    so for num = 2, 2 is not > 2*1
    for num = 3, 3 is greater than 2*1 so have at least one more reverse pair at this step 
    we need not to check further because as the list is sorted so all number greater than 3 
    will also form a reverse pair so we can directly add to reverse pair count

    now since 5 is will not be swapped so we not to check it reverse pair in the left
'''


def mergesort(array,start, end):
    if start >= end : return 0
    mid = (start+end) //2
    a=mergesort(array,start,mid)
    b=mergesort(array,mid+1,end)
    c=merge(array,start,mid,end,a+b)
    return c

def merge(array,start,mid,end,reverse):
    # print(start,mid,end)
    arr = [0]*(end-start+1)
    i=start
    j=mid+1
    while(i<mid+1):     #for every number in left array
        while(j<=end and array[i] > 2*array[j] ):   #check whether we have any element on right that satisfy the reverse pair condition
            reverse+=(mid-i+1)          #if so then all number after ith position will form pair with jth number as 1 will form pair with 3,4 in the above example
            j+=1    #check for all number in second array that satisfy the conditon
        i+=1    #increment i when the condition is not satisfied for some incremented j
    '''
    genral merge sort procedure
    '''
    i=start
    j=mid+1
    k=0
    while(i<mid+1 and j<=end):
        if array[i] > array[j] :
            arr[k] = array[j]
            j+=1
            k+=1
        else:
            arr[k] = array[i]
            i+=1
            k+=1
    while i < mid+1:
        arr[k] = array[i]
        i+=1
        k+=1
    while j <= end:
        arr[k] = array[j]
        j+=1
        k+=1
    for num in arr:
        array[start]=num
        start+=1
    return reverse

class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        return mergesort(nums,0,len(nums)-1)
        
        