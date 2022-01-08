class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        #code here
        self.ls =[]
        self.cap=cap
        self.mp={}
        
        
    #Function to return value corresponding to the key.
    def get(self, key):
        if key in self.mp:
            return self.mp[key]
        return -1
        #code here
        
        
    #Function for storing key-value pair.   
    def set(self, key, value):
        if key not in self.ls:
            if len(self.ls) >= self.cap : self.mp.pop(self.ls.pop())
        else:
            self.ls.remove(key)
        self.mp[key]=value  
        self.ls.insert(0,key)

ca = LRUCache(2)
ca.set(87,56)
ca.set(98,4)
ca.set(1,5)
print(ca.ls)
print(ca.get(87))
