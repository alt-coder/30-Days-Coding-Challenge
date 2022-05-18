class StockSpanner:
    '''
    using monotonic stack that means the value in the stack is strictly decreasing
    '''
    def __init__(self):
        self.stack=[(999999,0)]  #initial stack value is large (price,index)
        self.idx=0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price: #if top has val < price
            val,ix = self.stack.pop()   #keep popping
        
        top = self.stack[-1][1] #get the index of top i.e index of previous seen greater price than the current price
        
        self.idx+=1 # increment the number of values seen , i.e index of current price in an array
        self.stack.append((price,self.idx)) ##add it to stack
        return self.idx -top    #return the difference