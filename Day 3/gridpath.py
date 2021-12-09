""
def path(m,n,map):
    if n==1 or m==1:
        map[(m,n)] = 1
        return map[(m,n)]
    if (m,n) in map:
        return map[(m,n)]
    map[(m,n)] = path(m-1,n,map) + path(m,n-1,map)
    return map[(m,n)]
map ={(1,1):1}
print(path(3,2,map))