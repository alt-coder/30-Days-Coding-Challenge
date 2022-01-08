def lps(s):
    i=0
    j=1
    lp=[0]*len(s)
    while j < len(s):
        if s[i]==s[j]:
            i+=1
            lp[j]=i
            
        else:
           
            i=lp[i-1]
        j+=1
    return lp

lp = lps("AAACAAAAAC")
for i in lp:
    print(i,end=" ")


