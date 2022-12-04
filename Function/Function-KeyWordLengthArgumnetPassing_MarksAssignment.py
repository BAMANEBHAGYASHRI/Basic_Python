def marks(*m):
    for i in m:
        sum=0
        for j in i:
            sum=sum+j
        pre=sum/5
        print(pre)
        if(sum>=75 and sum<=90):
            print("Congoo !Frist class with dist--",pre)
            print("----------")
        elif(sum>=50 and sum<=75):
            print("congoo ! Frist Class...",pre)
        elif(sum>=35 and sum<=50):
            print("congo ! pass")
        elif(sum>=0 and sum<=35):
            print("Fail ! never give up...!!",pre)
    

    
marks([90,89,78,65,59],[90,87,65,45,29],[12,90,87,56,48],[90,76,54,23,99])

