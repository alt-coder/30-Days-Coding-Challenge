def compare(s,t):
    if len(s)>len(t):
        return 1
    if len(t) > len(s):
        return 2
    i=0
    while i <len(s):
        if s[i] > t[i] :
            return 1
        elif t[i] > s[i]:
            return 2
        i+=1
    return 0

def comp(s1, s2):
    i=j=0
    while i < len(s1) or j <len(s2):

        #ignore leading zero

        while(i<len(s1) and (s1[i]=='0' or s1[i]=='.')): i+=1
        while(j<len(s2) and (s2[j]=='0' or s2[j]=='.')): j+=1

        ## read till dot
        p=i
        q=j

        while i<len(s1) and s1[i] != '.':
            i+=1
        while j < len(s2) and s2[j] != '.': j+=1

        # compare the block
        res = compare(s1[p:i],s2[q:j])
        if res != 0:
            return res
        i+=1
        j+=1
    # if i>j : return 2
    # if j > i : return 1
    return 0

if __name__ == "__main__":
    version1 = '0000.14.21'
    version2 = '0014.21.01'
    print(comp(version1,version2))
