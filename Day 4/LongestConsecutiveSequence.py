def solve(arr):
    s={i for i in arr}      #List comprehension is slow
    ans=0
    for i in arr:           #iterating over an List is slow
        if i-1 not in s:
            it=i
            ct=1
            while it+1 in s:
                ct+=1
                it+=1
            ans= max(ct,ans)
    return ans

'''
Optimized python code
'''
def longestConsecutive(arr) -> int:
    s=set(arr)
    ans=0
    for i in s:
        if i-1 not in s:
            it=i
            ct=1
            while it+1 in s:
                ct+=1
                it+=1
            ans= max(ct,ans)
    return ans

print(solve([1, 9, 3, 10, 4, 20, 2]))

