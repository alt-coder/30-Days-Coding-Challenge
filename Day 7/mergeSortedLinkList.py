from LinkedList import LinkedList as List
from LinkedList import Node

def mergeAux(node1,node2):
    if node1 is None:
        return node2
    if node2 is None:
        return node1
    if node1.value < node2.value:
        node1.next = mergeAux(node1.next,node2)
        return node1
    else :
        node2.next = mergeAux(node2.next,node1)
        return node2

# def merge(ls1,ls2):
#     ls1.head.next = mergeAux(ls1.head.next,ls2.head.next)
#     return ls1

def mergeitr(node1,node2):
    p1 = node1
    p2 = node2
    res = Node(None)
    last = res
    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            last.next=p1
            p1 = p1.next
        else:
            last.next = p2
            p2 = p2.next
        last = last.next
    if p1 is None : last.next = p2
    if p2 is None : last.next = p1
    return res.next

def merge(ls1,ls2):
    ls1.next = mergeitr(ls1.head.next,ls2.head.next)
    return ls1

l1 = List().insert(1,3,9,10)
l2 = List().insert(2,4,5,6,78,87)
merge(l1,l2)
for i in l1:
    print(i)

