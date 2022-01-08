def calculateCurrentHash(s):
    d=52
    n=len(s)-1
    val=0
    for c in s:
        val += ((ord(c)-(ord('a')-1))*(52**n))
        n-=1
    return val

def rabin(s, p):
    target= calculateCurrentHash(p)
    n=nd=len(p)-1
    d=52
    val=0
    for c in s[:n+1]:
        val += (ord(c)-(ord('a')-1))*(52**nd)
        nd-=1
    sl=len(s)
    s+=" "
    for i in range(n,sl):
        if target==val:
            z=s[i-n:i+1]
            if p == z:
                print("found at ",i-n)
        val= (val - ((ord(s[i-n])-(ord('a')-1))*(52**n)))*52+ord(s[i+1])-(ord('a')-1)
        

rabin("shubham",'ub')
