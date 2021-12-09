
def GCD(n,m):
    while(m>0):
        r= n%m
        n=m
        m=r
    return n

def RGCD(n,m):
    if m==0:
        return n
    return RGCD(m,n%m)
print(GCD(20,5))
print(RGCD(5,22))