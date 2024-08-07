       
    
def isPalindrom(n):
    return str(n)==str(n)[::-1]

l = [x for x in range (100000,1000000) if isPalindrom(x)]

print (l)
