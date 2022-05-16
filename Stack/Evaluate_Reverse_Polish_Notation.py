def evalRPN(tokens: list[str]) -> int:
        stack=[]
        operators = {'*','+','-',"/"}
        for token in tokens:
            if token in operators:
                a = int(stack.pop())
                b=int(stack.pop())
                ans=0
                if token == '*': ans=a*b  
                elif token == "/": ans = int(b/a)
                elif token == '+':  ans = a+b
                else: ans = b-a
                stack.append(ans)
            else: stack.append(token)
        return stack[0]

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))