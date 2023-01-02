def sorting(*string):
    for i in string:
        a= ""
        b = ""
        c = ""
        d = ""

        for j in i:
            if (ord(j) >= 65 and ord(j) <= 90):
                a= j +a
            elif (ord(j) >= 97 and ord(j) <= 122):
                b = j + b
            elif (ord(j) >= 46 and ord(j) <= 52):
                c = j +c
            elif ((ord(j) >= 58 and ord(j) <= 64) or (ord(j) >= 91 and ord(j) <= 96) or (ord(j) >= 32 and ord(j) <= 47)):
                d = j + d

        # print("captical Charachter--",a)
        # print("small Charachter--", b)
        # print("number--", c)
        # print("specail symbol --", d)
        print(a,b,c,d)


sorting("^&*$6790BHhadauyqkjeiueiuHJDUYUYWP870264$$^")