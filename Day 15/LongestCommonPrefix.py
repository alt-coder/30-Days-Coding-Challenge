def findPrefix(st1,st2):
    prefix=''
    for i in range(len(st1)):
        if st1[i] == st2[i]:
            prefix+=st1[i]
        else:
            break
    return prefix
def LongestCommon(lis):
    # ls= sorted(lis,key= lambda x:len(x))
    lis.sort(key= lambda x:len(x))
    prefix=lis[0]
    for st in lis[1:]:
        prefix=findPrefix(prefix,st)
    return prefix


