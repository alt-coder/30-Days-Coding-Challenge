def substr(s,length):
    '''all substring function based on length'''
    if (length == 0):
        return
    substr(s,length-1)
    for i in range(len(s)-length+1):
        print(s[i:i+length])
    
def substr_start(s,start):
    '''all substring function based on startindex'''
    if (start==len(s)):
        return

    for i in range(start+1,len(s)+1):
        
        if start+1 == i :substr_start(s,i)
        print(s[start:i])
s="abcde"
substr(s,5)
substr_start(s,0)