def check(string):
    n= len(string)
    # mp=[[1 if i==j or(abs(i-j) ==1 and string[i]==string[j]) else 0 for i in range(n)] for j in range(n)]
    # # for i in range(n-1):
    #     if string[i] == string[i+1]:
    #         mp[i][i+1]=1
    mp=[[False]*n for i in range(n)]
    count=a=b=0
    for  i in reversed(range(n)):
        for j in range(i,n):
            if i == j :
                        mp[i][j]=True
                        if i>0 and string[i]==string[j-1]: mp[i][j-1]=True
                        if j+1<n and string[i]==string[j+1]: mp[i][j+1]=True
                        continue
            if i+1 <= j and string[i]==string[j] and mp[i+1][j-1]:
                mp[i][j]=True
                if count <= j-i:
                        a=i
                        b=j
                        count=j-i

    return string[a:b+1]

print(check("qbbc"))
