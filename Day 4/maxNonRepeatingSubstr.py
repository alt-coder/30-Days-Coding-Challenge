def find(st):
     mp = dict()
     ct=startindex=0
     for i in range(len(st)):
        if st[i] in mp:
             if mp[st[i]] >= startindex  :startindex = mp[st[i]]+1      #if we have seen the seq and making sure startindex is always increasing
             mp[st[i]] =i
        else:
            mp[st[i]] =i
            ct = max(i-startindex,ct)   #count value only changes when we have seen a new character
     return ct+1

print(find("aaaaaabcaaabcderabcdefgtya"))