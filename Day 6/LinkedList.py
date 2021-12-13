class Node:
    def __init__(self,val) -> None:
        self.value = val
        self.previous = None
        self.next = None
        self.back = None
        

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.last = self.head
        self.size = 0
        self.current = self.head
        return None
    def __len__(self):
        return self.size
    def insert(self,*args):
        for val in args:
            n = Node(val)
            last = self.last
            self.last.next = n
            self.last = n
            n.back = last
            self.size+=1
        return self
    def insertFront(self,*items):
        for val in items:
            n = Node(val)
            if self.head.next is not None:
                n.next = self.head.next
                self.head.next.back = n
                n.back = self.head
                self.head.next = n
            else:
                last = self.last
                self.last.next = n
                self.last = n
                n.back = last
            self.size+=1
        return self

    def __iter__(self):
        return self
    def __next__(self):
        self.current = self.current.next
        if self.current:
            val = self.current.value
            return val
        else:
            self.current = self.head
            raise StopIteration
            
    def find(self,val):
        nxt = self.head.next
        while nxt:
            if nxt.value == val:
                return True
            else:
                nxt = nxt.next
        return False
    def __contain__(self,val):
        return self.find(val)

    
