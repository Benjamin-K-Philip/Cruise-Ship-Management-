#nuskaerrors
import nuskatimeerrors
import sys
def nuskaerr():
    f=open("nuskatext.txt",'r')
    d=f.read()
    print(d)
    print("")
    name=input("Please enter a valid name:")
    res=input("\nWould you like to book a table at our restaurant?(Yes/No):")
    if res in "YES Yes yes Y y":
        nuska=open('nuska.txt','a+')
        table=int(input("\nHow many guests are we expecting?:"))
        print("""\nBelow are the time slots provided for dining in 
    1.)8:00 -11:30 --->  Breakfast
    2.)11:30-13:00 --->  Brunch
    3.)13:00-16:00 --->  Lunch
    4.)16:00-18:00 --->  Refreshments
    5.)18:00-23:00 --->  Dinner""")        
        time=int(input("Enter a valid time slot(1/2/3/4/5):"))
        t=""
        if time==1:
            tim="8:00 -11:30 ---> Breakfast "
            t=t+tim
        elif time==2:
            tim="11:30-13:00 --->  Brunch "
            t=t+tim
        elif time==3:
            tim="13:00-16:00 --->  Lunch "
            t=t+tim
        elif time==4:
            tim="16:00-18:00 --->  Refreshments "
            t=t+tim
        elif time==5:
            tim="18:00-23:00 --->  Dinner "
            t=t+tim
        else:
            print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
            #Giving user a second attempt to enter a valid choice
            print("")
            nuskatimeerrors.nuskatimerr()
        print("\nAlright",name,", table for",table,"is reserved for",t)
        a=name+','+str(table)+','+ t
        nuska.write(a)
        print("""We look forward to giving you the best dining experience.
Have a great day!""")
    elif res in "NO No no N n":
        print("\nThank you for visiting Nuska beach.")
    else:
        print("\nAn invalid choice is entered.")
        sys.exit()

