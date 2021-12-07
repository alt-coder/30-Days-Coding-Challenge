def meroverlap(arr):
    if len(arr) == 0:
        return arr
    st = sorted(arr,key= lambda x:(x[0],-x[1])) #sort the interval and incase of tie make sure large end interval come first
    ans =[]
    ans.append(st.pop(0))       #append the first element as it is
    while st:
        if ans[-1][1] >= st[0][0]:      #if last element end is >= sorted list start
            ans[-1][1] = max(st[0][1],ans[-1][1])   #merge them
        else :
            ans.append(st.pop(0))       #else append the interval as it is
    return ans


    