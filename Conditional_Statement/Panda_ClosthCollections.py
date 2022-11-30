print("------ <<<WELCOME TO PANDA CLOTH COLLECTION",u"\U0001F43C>>> ------")
cloth=input("What You Want ? (catgory men=1 women=2 kids=3)")
if(cloth=="1"):
    cloth_for_mens=input("which type ? (shirt=1 jeans=2)")
    if(cloth_for_mens=="1"):
        Type_of_shirts=input("select types of shirts---formal_shirts-1 causal_Shirts-2 T-shirt=3 ")
        if(Type_of_shirts=="1"):
            formal_shirts=input("Select   TYpes Of Formal Shirts---[Modern-Fit Dress Shirts=1 Slim Fit Dress Shirts=2 Skinny Fit Dress Shirts=3 Straight Point Collar=4] ")
            if(formal_shirts=="1"):
                print("show me the  Modern-Fit Dress Shirts ")
            elif(formal_shirts=="2"):
                print("show me the Slim Fit Dress Shirts")
            elif (formal_shirts == "3"):
                print("show me the Skinny Fit Dress Shirts")
            elif (formal_shirts == "4"):
                print("show me the Straight Point Collar")
        elif(Type_of_shirts=="2"):
            causal_Shirts = input("Select  TYpes Of causal shirts---[Button-Down Collar Shirts=1 Utility Shirts=2 Shirt Jackets=3 Band Collar Shirts=4] ")
            if (causal_Shirts == "1"):
                print("show me the Button-Down Collar Shirts ")
            elif (causal_Shirts == "2"):
                print("show me the Utility Shirts")
            elif (causal_Shirts == "3"):
                print("show me the Shirt Jackets")
            elif (causal_Shirts == "4"):
                print("show me the Band Collar Shirts")
        elif(Type_of_shirts=="3"):
            T_shirt = input("Select  Types Of Tshirts--[Half Sleeves T-Shirts=1  V-Neck T-Shirts=2  3=Solid T-Shirts 4=Striped T-Shirts]")
            if (T_shirt == "1"):
                print("show me the Half Sleeves T-Shirts")
            elif (T_shirt== "2"):
                print("show me the V-Neck T-Shirts")
            elif (T_shirt == "3"):
                print("show me  theSolid T-Shirts")
            elif (T_shirt == "4"):
                print("show me the Striped T-Shirts")

    elif (cloth_for_mens == "2"):
        Type_of_pants = input("select types of pants---Trousers-1 pants-2 Jeans=3 ")
        if (Type_of_pants == "1"):
            Traousers = input("Select   TYpes Of Traousers---[Corduroy Trousers=1  Wool Trousers=2 Linen Trousers=3 Drawstring Trousers=4] ")
            if (Traousers == "1"):
                print("show me the  Corduroy Trousers ")
            elif (Traousers == "2"):
                print("show me the Wool Trousers")
            elif (Traousers == "3"):
                print("show me the Linen Trousers")
            elif (Traousers == "4"):
                print("show me the Drawstring Trousers")

        elif (Type_of_pants == "2"):
            Pants = input("Select  TYpes Of Pants---[ Pleated Pants=1 Dress Pants=2 Cargo Pants=3Lounge Pants=4] ")
            if (Pants == "1"):
                print("show me the  Pleated Pants ")
            elif (Pants == "2"):
                print("show me theDress Pants")
            elif (Pants== "3"):
                print("show me the Cargo Pants")
            elif (Pants == "4"):
                print("show me the Lounge Pants")

        elif (Type_of_pants == "3"):
            Jeans= input("Select  Types Of Jeans--[Slim Fit Jeans=1 Skinny Fit Jeans=2  Regular Fit Jeans=3 Tapered Fit=4]")
            if (Jeans == "1"):
                print("show me the Slim Fit Jeans")
            elif (Jeans == "2"):
                print("show me the Skinny Fit Jeans")
            elif (Jeans== "3"):
                print("show me  Regular Fit Jeans")
            elif (Jeans== "4"):
                print("show me Tapered Fit")

elif(cloth=="2"):
    cloth_for_women= input("which type ? (Kurties=1 sadi=2 top=3 jeans=4)")
    if (cloth_for_women == "1"):
        Type_of_kurtie = input("select types of Kurtiss kurties=1")
        if (Type_of_kurtie == "1"):
            kutries = input("Select   TYpes Of Kutries---[Frock Kurti=1 A-Line Kurti=2  Anarkali Kurti=3 Trail Cut Kurti=4] ")
            if (kutries == "1"):
                print("show me the  Frock Kurti ")
            elif (kutries == "2"):
                print("show me the A-Line Kurti")
            elif (kutries == "3"):
                print("show me the Anarkali Kurti")
            elif (kutries == "4"):
                print("show me the Trail Cut Kurti")
    elif(cloth_for_women == "2"):
        Type_of_sari = input("select types of Saris=2")
        if (Type_of_sari == "2"):
            sari = input("Select  Sareee---[Kanchipuram silk sari=1 Paithani=2 Banarasi sari=3 Baluchari sari=4] ")
            if (sari== "1"):
                print("show me the Kanchipuram silk sari ")
            elif (sari == "2"):
                print("show me the Paithani")
            elif (sari == "3"):
                print("show me the Banarasi sari")
            elif (sari == "4"):
                print("show me the Baluchari sari")

        elif (cloth_for_women == "3"):
            Type_of_topJeans = input("select types of Top=3")
            if (Type_of_topJeans == "2"):
                topsjeans = input("Select  Sareee---[Blouse Top & Bell-bottoms=1 Crop Top & Mom jeans=2 Tank Top & Wide-leg jeans=3 Cami Top & Slim-fit pants=4] ")
                if (topsjeans== "1"):
                    print("show me theBlouse Top & Bell-bottoms ")
                elif (topsjeans == "2"):
                    print("show me the Crop Top & Mom jeans")
                elif (topsjeans == "3"):
                    print("show me the Tank Top & Wide-leg jeans")
                elif (topsjeans == "4"):
                    print("show me the Cami Top & Slim-fit pants")

elif(cloth=="3"):
    cloth_for_kids= input("which type ? (Boys=1 Girls=2)")
    if (cloth_for_kids == "1"):
        Type_of_ShirtsPants = input("select types of Shirts and pants=1")
        if (Type_of_ShirtsPants == "1"):
            boyz = input("Select   TYpes Of Kutries---[Frock Kurti=1 A-Line Kurti=2  Anarkali Kurti=3 Trail Cut Kurti=4] ")
            if (boyz == "1"):
                print("show me the  Frock Kurti ")
            elif (boyz == "2"):
                print("show me the A-Line Kurti")
            elif (boyz == "3"):
                print("show me the Anarkali Kurti")
            elif (boyz == "4"):
                print("show me the Trail Cut Kurti")










