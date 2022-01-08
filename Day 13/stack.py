from LinkedList import LinkedList as List
class Stack(List):
    def __init__(self):
        super().__init__()
    def pop(self):
        return self.remove()
    def top(self):
        return self.last.value
    def isEmpty(self):
        return True if self.size ==0 else False

if __name__ =='__main__':
    a = Stack()
    a.insert(1)
    a.insert(2)
    print(a.pop())
    print(a.top())
    print(a.isEmpty())
    print(a.pop())
    print(a.isEmpty())