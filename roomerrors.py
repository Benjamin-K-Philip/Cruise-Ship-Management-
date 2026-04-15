#roomerrors
import random
def roomerr():
    print("\n1.)regular suite-1,200 AED \n2.)premium suite-3,000 AED")
    cruisetype=int(input("Please enter room you prefer(1/2):"))
    roomtype=" "
    price=0
    if cruisetype==1:
        roomtype="Regular suite"
        price+=3000
        print("Your ticket has been booked!")   
        roomno=random.randint(1,500)
    elif cruisetype==2:
        roomtype="Premium suite"
        price+=1200
        print("Your ticket has been booked!")
        roomno=random.randint(1,500)
    else: 
        print("""Wrong choice is entered.
    Please enter a valid choice given from the above options.""")












    
