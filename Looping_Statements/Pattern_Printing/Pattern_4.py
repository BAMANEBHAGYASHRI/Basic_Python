# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()
for k in range(5):
    for l in range(5-k):
        print("*", end="")
    print()