def Stringsorting(*str):
    for i in str:
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


        # print("specail symbol --", d)
        return  a,b,c,d


if(__name__=="__main__"):
    Stringsorting()