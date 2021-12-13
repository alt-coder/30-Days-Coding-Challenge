
from LinkedList import LinkedList as List
def check(lst):
    if len(lst) <=1 : return True
    s= len(lst)//2
    i=0
    temp = lst.head
    while i !=s:
        temp=temp.next
        i+=1
    #reverse from next element
    if len(lst)%2 ==0 : current = temp.next
    else: current = temp.next.next
    previous = None
    while current != None :
        nxt = current.next
        current.next = previous
        previous=current
        current=nxt
    last_revnode=previous
    i=0
    ans=True
    first=lst.head.next
    while i !=s:
        if first.value != previous.value:
            ans=False
            break
        first=first.next
        previous = previous.next
        i+=1
    #Re reverse the list we had reversed
    current=last_revnode
    previous=None
    while current != None :
        nxt = current.next
        current.next = previous
        previous=current
        current=nxt
    return ans
l1=List().insert(1,2,1)
print(check(l1))
for i in l1:
    print(i)

    