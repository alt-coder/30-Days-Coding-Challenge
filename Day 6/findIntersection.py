# consider two a single ended linked list
from  LinkedList import LinkedList as List
def find(list1,list2):
    d = abs(len(list1)-len(list2))
    big = list1.head.next if len(list1) >= len(list2) else list2.head.next
    small = list2 if len(list1) > len(list2) else list1
    while d>0 :         #traverse the bigger list till both the list has same numbers of elements
        big=big.next
        d-=1
    s = len(small)
    small=small.head.next
    while s:            # traverse both the list and check if the nodes are same or not
        if big.value == small.value :       #only value is compared because of simplicity while testing
            return big.value 
        big = big.next
        small =small.next
        s-=1
    return None

l1 = List().insert(1,2,3,4,5)
l2 = List().insert(6,3,4,5)     # 3 is intersection point

print(find(l1,l2))