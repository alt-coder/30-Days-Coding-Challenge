def substr(s,length):
    '''all substring function based on length'''
    if (length == 0):
        return
    substr(s,length-1)# decrement the length and print those
    for i in range(len(s)-length+1):
        print(s[i:i+length])
    
def substr_start(s,start):
    '''all substring function based on startindex'''
    if (start==len(s)):
        return

    for i in range(start+1,len(s)+1):
        print(s[start:i])
        if start+1 == i :substr_start(s,i)
        #print(s[start:i])
def subs(s,ans,start,i):
    '''printing substing based on inclusion exclusion
    start : index of next char to be appended to the ans
    i: index of last character appended to the ans'''
    if start == len(s):
        print(ans)
        return
    
    if(i==-1 or start-i <= 1):subs(s,ans+s[start],start+1,start)#to make sure that we print substring not sub sequence
    else:#if we have ever skiped a character(except skipping initial chars) then we shall never contiue further
        print(ans)
        return 
    subs(s,ans,start+1,i) #dont take a charter
s="abcd"
# substr(s,5)
substr_start(s,0)
print()
subs(s,"",0,-1)