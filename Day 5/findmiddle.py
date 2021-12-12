from LinkedList import LinkedList as List
def findmiddle(lst):
    sz = len(lst) // 2
    ct=0
    for it in lst:
        if ct == sz :
            return it
        ct+=1

l = List()
l.insert(1,2,3,4,5)

print(findmiddle(l))