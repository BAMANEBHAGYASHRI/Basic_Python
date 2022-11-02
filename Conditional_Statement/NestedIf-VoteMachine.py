voterage=int(input("Enter your age: "))
if(voterage>18):
    print("Voter is eligible")
    a=input("Do you have Voter Id")
    if(a=="Yes"):
        print("you can vote")
    else:
        print("Bring Youe voter ID")
else:
    print("voter is not eligible")