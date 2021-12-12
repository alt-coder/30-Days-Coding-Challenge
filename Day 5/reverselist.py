from LinkedList import LinkedList as List
def reverse(lst):
    if type(lst) == List:
        lastnode= lst.last
        res = List()
        while lastnode.value is not None:
            res.insert(lastnode.value)
            lastnode=lastnode.back
        return res
    

l = List()

l.insert(1,2,3,4)
for it in l:
    print(it)
rev = reverse(l)

for i in rev:
    print(i)
