def Sum(arr,target):
    hasht=set()
    for it in arr:
        if target-it in hasht:
            return True
        else :
            hasht.add(it)
    return False

arr=[1,2,3,4,5,6]

print(Sum(arr,19))