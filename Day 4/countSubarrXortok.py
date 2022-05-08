


def count(arr,k):
    #a = set(arr)
    mp=dict()
    ct=0
    cuurxor=0
    for item in arr:
        cuurxor = item ^ cuurxor
        if cuurxor == k : ct+=1
        y = cuurxor ^ k
        if y in mp : ct+=mp[y]
        if cuurxor in mp :mp[cuurxor]+=1
        else: mp[cuurxor]=1
    return ct

print(count([4,2,2,6,4],6))