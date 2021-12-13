#https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/

from LinkedList import LinkedList as List


def rev(node,k):
    if node is None : return None
    current = node
    previous = None
    count =0
    while current is not None and count < k :
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt
        count+=1
    if current is None : return previous
    node.next = rev(nxt,k)
    return previous

def reverse(lst,k):
    if lst.head.next is not None:
        lst.head.next = rev(lst.head.next,k)
    return lst

l = List().insert(1,2,3,4,5,6,7,8)

l2 = reverse(l,3)

for i in l2:
    print(i)
