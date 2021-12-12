from LinkedList import LinkedList as List
def add(ls1,ls2):
    l1=ls1.last
    l2=ls2.last
    res = List()
    r=0
    while l1.value is not None and l2.value is not None:
        q=l1.value + l2.value +r
        if q >= 10:
            r = q//10
            q = q%10
        else: r = 0
        res.insertFront(q)
        l1=l1.back
        l2=l2.back
    lst = l1 if l2.value == None else l2
    while lst.value is not None :
        val = lst.value +r
        if val >= 10:
            r= val//10
            val%=10
        else:
            r=0
        res.insertFront(val)
        lst = lst.back
    if r!=0: res.insertFront(r)
    return res

l1=List().insert(9,0,9)
l2=List().insert(9,1,9)
l3 = add(l1,l2)

for i in l3:
    print(i,end="")