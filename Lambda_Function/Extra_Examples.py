def demolambda(n):
    return lambda x:x+n

f=demolambda(90)
print(f(9))


pairs=[(1,'one'),(2,'two'),(3,'three')]
print(pairs.sort(key=lambda pair:[1]))
print(pairs)
