#fikaerrors
import sys
import fikatimeerrors
def fikaerr():
    f=open("fikatext.txt",'r')
    d=f.read()
    print(d)
    print("")
    name=input("Please ener a valid name:")
    res=input("\nWould you like to book a table at our restaurant?(Yes/No):")
    if res in "YES Yes yes Y y":
        fika=open('fika.txt','a+')
        table=int(input("\nHow many guests are we expecting?:"))
        print("""Below are the time slots provided for dining in 
    1.)12:00-16:00 ---> Lunch
    2.)18:00-22:00 ---> Dinner""")
        time=int(input("What time would you like to dine with us?(1/2):"))
        t=""
        if time==1:
            tim="12:00-16:00 ---> Lunch "
            t=t+tim
        elif time==2:
            tim="18:00-22:00 ---> Dinner "
            t=t+tim
        else:
            print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
            #Giving user a second attempt to enter a valid choice
            print("")
            fikatimeerrors.fikatimerr()
        print("\nAlright,",name,"table for",table,"is reserved for,",t)
        a=name+','+str(table)+','+ t
        fika.write(a)
        fika.close()
        print("""We look forward to giving you the best dining experience.
Have a great day!""")
    elif res in "NO No no N n":
        print("\nThank you for visiting Fika.")
    else:
        print("\nAn invalid choice is entered.")
        sys.exit()

