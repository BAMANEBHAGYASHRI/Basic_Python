def digitalnumber(*number):
    add = 0
    p = 0
    q = 0
    t=0
    for i in number:
        add= add + int(i)
    print(add)
    s = str(add)
    if (len(s) > 1):
        for j in s:
            p = p + int(j)
        print(p)
    s = str(p)
    if (len(s) > 1):
        for r in s:
            q = q + int(r)
        print(q)
    s = str(t)
    if (len(s) > 1):
        for u in s:
            u = u + int(t)
        print(u)


digitalnumber(897899)