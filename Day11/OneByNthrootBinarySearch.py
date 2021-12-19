def find(num,n):
    low=0.01
    high=num/n if num>1 and n>2 else num
    
    while (high-low >=0.001): #limit the precision
        test = low+((high-low)/2)
        if test == low or test == high:
            return test         #sometimes due to precision they can become equal so break
        val = test**n
        if val > num:
            high=test
        elif val < num:
            low= test
        else:
            return test
    return test+0.0005
print(find(3,2))