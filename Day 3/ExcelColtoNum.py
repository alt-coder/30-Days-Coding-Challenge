'''
Similar to decimal system just the base is 26 here
'''
def ExcelColToNum(st):
    factor = 1
    res=0
    for ch in reversed(st):
        res += (factor) * (ord(ch) - (ord('A') - 1) )
        factor *= 26
    return res

print(ExcelColToNum('Z'))
print(ExcelColToNum('AA'))
print(ExcelColToNum('AAA'))