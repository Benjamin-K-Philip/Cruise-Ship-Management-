#bastionerrors
import sys
import bastiontimeerrors
def bastionerr():
    f=open("bastiontext.txt",'r')
    d=f.read()
    print(d)
    print("")
    name=input("Please enter a valid name:")
    res=input("\nWould you like to book a table at our restaurant?(Yes/No):")
    print("")
    if res in "YES Yes yes Y y":
        bastion=open('bastion.txt','a+')
        table=int(input("\nHow many guests are we expecting?:"))
        print("""Below are the time slots provided for dining in 
    1.)12:30-15:00 ---> Lunch
    2.)18:00-23:00 ---> Dinner and Bar""")
        time=int(input("What time would you like to dine with us?(1/2):"))
        t=""
        if time==1:
            tim="12:30-15:00 ---> Lunch "
            t=t+tim
        elif time==2:
            tim="18:00-23:00 ---> Dinner and Bar "
            t=t+tim
        else:
            print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")   
            #Giving user a second attempt to enter a valid choice
            print("")
            bastiontimeerrors.bastiontimerr()
        print("\nAlright,",name,"table for",table,"is reserved for,",t)
        a=name+','+str(table)+','+ t 
        bastion.write(a)
        bastion.close()
        print("""We look forward to giving you the best dining experience.
Have a great day!""")
        pass
    elif res in "NO No no N n":
        print("\nThank you for visiting Bastion.")
    else:
        print("\nAn invalid choice is entered.")
        sys.exit()
