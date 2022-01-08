from stack import Stack
def checkBalance(string):
    a=Stack()
    for ch in string:
        if ch == ')' and a.top() != '(':
            return False
        if ch == ')' and a.top() == '(':
            a.pop()
        if ch == '(':
            a.insert(ch)
        
        
        
    return a.isEmpty()

print(checkBalance('(25+96)+(89+9)()'))