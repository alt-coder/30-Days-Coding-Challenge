# '''
# Please take extra care to make sure that you are type-casting your ints to long properly and at all places. Try to verify if your solution works if number of elements is as large as 105

# Food for thought :

# Even though it might not be required in this problem, in some cases, you might be required to order the operations cleverly so that the numbers do not overflow.
# For example, if you need to calculate n! / k! where n! is factorial(n), one approach is to calculate factorial(n), factorial(k) and then divide them.
# Another approach is to only multiple numbers from k + 1 ... n to calculate the result.
# Obviously approach 1 is more susceptible to overflows.
# You are given a read only array of n integers from 1 to n.

# Each integer appears exactly once except A which appears twice and B which is missing.

# Return A and B.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Note that in your output A should precede B.

# Example:

# Input:[3 1 2 5 3] 

# Output:[3, 4] 

# A = 3, B = 4
# '''

def find(arr):
    '''
    find sumN = sum of array - sum of all the numbers from 1 to n
            = repeated-missing
       =>repeated = sumN+missing 
    find sumsqr = (sum of array)^2 - (sum of all the numbers from 1 to n)^2
                = repeated^2 - missing^2
                =(repeated - missing)(repeated+missing)
                = sumN * (sumN+ 2 *missing)
        missing = ((sumsqr/sumN)-sumN) // 2
    '''
    sumN = 0
    sumSqr =0
    for i in range(len(arr)):
        sumN = sumN+ (arr[i]-(i+1))
        sumSqr = sumSqr+ (arr[i]**2-(i+1)**2)
    missing = int(((sumSqr/sumN)-sumN) // 2)
    repeated = int(sumN+missing)

    return [missing,repeated]

arr = [1,2,2,3,5]

print(find(arr))
    
        
