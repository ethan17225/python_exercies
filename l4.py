def isEven (n):
    return  n%2==0
        
    
def isPrime(n):
    if isEven(n):
        return False
    
    for d in range(3,n//2, 2):
        if n%d==0:
            return False

    return True

l = [x for x in range (0,100) if isPrime(x)]

print (l)
