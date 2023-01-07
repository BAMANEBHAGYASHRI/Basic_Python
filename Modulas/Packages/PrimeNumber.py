def prime(a):
    b = a // 2
    state = 0
    for i in range(2, a):
        if (i % 2 == 0):
            state = i
            break
    if (state == 1):
        print(" not prime")
    else:
        print("prime")


if(__name__=="__main__"):
    prime()