
def pow(n,x):
    if x==0:
        return 1
    p = pow(n,x//2)
    if x%2 ==0 :
        return p*p
    else:
        return n *p*p

print(pow(2,4))
print(pow(5,3))
print(pow(-4,3))