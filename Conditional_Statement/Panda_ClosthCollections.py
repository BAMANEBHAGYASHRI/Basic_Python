print("------ <<<WELCOME TO PANDA CLOTH COLLECTION",u"\U0001F43C>>> ------")
cloth=input("What You Want ?")
if(cloth=="yes"):
    print("what types of clothes do you like ?(adult-A & Kids-K)")
    a=input("What you want form adult")
    k = input("What you want from Kidsy")
    if(a=="A"):
        b=input("shirts ya jeans(shirts-S & jeans-J)")
        # for shirts
        if(b=="S"):
            x=input("what type of T-shirts ?(-enter X Y Z)")
            if(x=="X"):
                print("Printed Men Round Neck Black T-Shirt")
            if(x=="Y"):
                print("Men Regular Fit Printed Spread Collar Casual Shirt")
            if(x=="Z"):
                print("Printed Men Round Neck White T-Shirt")
        # for jeans
        if(b=="J"):
            y = input("what type of Jeans ?(-enter X,Y,Z)")
            if (y == "X"):
                print("Slim Men Black Jeans")
            if (y == "Y"):
                print("Regular Men Grey Jeans")
            if (y == "Z"):
                print("Tapered Fit Men Blue Jeans")

        if (k == "K"):
            b = input("Boys and Girls (Boys-B & Girls-G)")
        # for baby Boys
            if (b == "B"):
                x = input("what type of Baby boys Dress ?(-enter X,Y,Z)")
                if (x == "X"):
                    print("Boys Printed Cotton Blend T Shirt")
                if (x == "Y"):
                    print("Full Sleeve Colorblock Boys Casual Jacket")
                if (x == "Z"):
                    print("Boys Regular Fit Solid Casual Shirt")
        # for baby girls-z=
            if (b == "G"):
                y = input("what type of baby girls dress?(-enter X,Y,Z)")
                if (y == "X"):
                    print("Baby Girls Short/Mid Thigh Casual Dress")
                if (y == "Y"):
                    print("Girls Party Cotton Blend Top")
                if (y == "Z"):
                    print("Girls Below Knee Party Dress  ")
else:
    print("Envalid Value")