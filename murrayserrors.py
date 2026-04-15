#murrayserrors
import sys
import murraystimeerrors
def murrayserr():
    f=open("murraystext.txt",'r')
    d=f.read()
    print(d)
    print("")
    name=input("Enter a valid name:")
    res=input("\nWould you like to book a table at our restaurant?(Yes/No):")
    print("")
    if res in "YES Yes yes Y y":
        murrays=open('murrays.txt','a+')
        table=int(input("How many guests are we expecting?:"))
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
            murraystimeerrors.murraystimerr()
        print("\nAlright,",name,"table for",table,"is reserved for,",t)
        a=name+','+str(table)+','+ t
        murrays.write(a)
        murrays.close()
        print("""We look forward to giving you the best dining experience.
Have a great day!""")
    elif res in "NO No no N n":
        print("\nThank you for visiting Murray's.")
    else:
        print("\nAn invalid choice is entered.")
        sys.exit()
       
