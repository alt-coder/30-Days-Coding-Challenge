from LinkedList import LinkedList as List
class LRU(List):
    def __init__(self,limit=1) -> None:
        self.limit=limit
        super().__init__()
        self.mp={}
    def refer(self,num):
        if num not in self.mp:
            if self.size > self.limit : self.remove()
            self.insertFront(num)
            self.mp[num]=self.head.next
        else:
            self.insertFront(num)
            nd=self.mp[num]
            self.mp[num]=self.head.next
            if nd.next is None:
                self.last=nd.back
                self.last.next=None
                del nd
            else:
                nd.back.next=nd.next
                nd.next.back=nd.back
                del nd
            

if __name__ == "__main__":
    ca = LRU(4)
    ca.refer(1)
    ca.refer(2)
    ca.refer(3)
    ca.refer(1)
    ca.refer(3)
    ca.refer(5)
    for item in ca:
        print(item)

