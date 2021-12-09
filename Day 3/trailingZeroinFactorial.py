"only compute number of 5 in the factorial"
def solve(num):
    i=5
    count=0
    while(num//i >= 1 ):
        count += num//i
        num = num//i
    return count

print(solve(100))