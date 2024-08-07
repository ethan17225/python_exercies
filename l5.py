def isEven (n):
    return  n%2==0
        
    
def isArmstrong(n):
    p = len(str(n))
    s = 0

    for d in str(n):
        s += int(d) ** p

    return n==s

l = [x for x in range (0,100000) if isArmstrong(x)]

print (l)
