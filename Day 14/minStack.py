class minStack:
    def __init__(self) -> None:
        self.stack=[]
        self.minElement=None
    def push(self,ele):
        if self.minElement != None:
            if self.minElement < ele:
                self.stack.append(ele)
            else:
                self.stack.append((2*ele) - self.minElement)
                self.minElement=ele
        else:
            self.stack.append(ele)
            self.minElement = ele
    
    def pop(self):
        minele=-1
        if len(self.stack) == 0:
            return None
        if self.stack[-1] >= self.minElement:
            return self.stack.pop()
        else:
            minele = self.minElement
            self.minElement= 2*self.minElement-self.stack[-1]
            self.stack.pop()
        if len(self.stack) == 0:
            self.minElement=None
        return minele
            
    def getMin(self):
        return self.minElement

st= minStack()
a= [18,19,29,15,16]
for ar in a:
    st.push(ar)
print(st.getMin())
st.pop()
st.pop()
print(st.getMin())