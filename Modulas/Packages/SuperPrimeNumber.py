def prime(a):
    b = a // 2
    state = 0
    for i in range(2, a):
        if (i % 2 == 0):
            state = i
            break
    if (state == 1):
        return False, a
    else:
        return True, a
def superprime(x,y):
    if (x == True):
        z = len(str(y))
        if (z >= 2):
            s = 0
            for j in str(y):
                s = s + int(j)
            p, q = prime(s)

            if (x == True):
                return True
            else:
                return False
        else:
            return False

if(__name__=="__main__"):
    x,y=prime(31)
    print("prime number",x)
    xyz=superprime(x,y)
    print("super prime number",x)



