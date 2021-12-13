from LinkedList import LinkedList as List

'''Rotate matrix clock wise'''
def rotate(lst,k):
    if k == 0: return lst
    head = lst.head
    previous = lst.last
    current= head.next
    count =0
    while count < k:
        next = current.next
        previous.next = current
        previous = current
        current = next
        count+=1
    head.next = current
    previous.next = None
    lst.last = previous
    return lst

l = List().insert(1,2,3,4,5,6)

for i in rotate(l,2):
    print(i)