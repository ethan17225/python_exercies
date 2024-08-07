def isEven (n):
    return  n%2==0
        
    
def isPrime(n):
    if isEven(n):
        return False
    
    for d in range(3,n//2, 2):
        if n%d==0:
            return False

    return True


n = 0
l=[]
while n<100:
    
    if isPrime(n):
        l.append(n)

    n+=1


print (l)
