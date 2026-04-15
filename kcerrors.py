#kcerrors
import sys
import kctimeerrors
def kcerr():
    f=open("KCtext.txt",'r')
    d=f.read()
    print(d)
    print("")
    name=input("Please enter a valid name:")
    res=input("\nWould you like to book a table at our restaurant?(Yes/No):")
    if res in "YES Yes yes Y y":
        Kc=open('KC.txt','a+')
        table=int(input("\nHow many guests are we expecting?:"))
        print("""Below are the time slots provided for dining in 
    1.)07:00-11:00 ---> Breakfast
    2.)18:00-23:00 ---> Dinner""")
        time=int(input("What time would you like to dine with us?(1/2):"))
        t=""
        if time==1:
            tim="07:00-11:00 ---> Breakfast "
            t=t+tim
        elif time==2:
            tim="18:00-23:00 ---> Dinner "
            t=t+tim
        else:
            print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
            #Giving user a second attempt to enter a valid choice
            print("")
            kctimeerrors.kctimerr()
        print("\nAlright,",name,"table for",table,"is reserved for,",t)
        print("""We look forward to giving you the best dining experience.
Have a great day!""")
        a=name+','+str(table)+','+ t
        Kc.write(a)
        Kc.close()
    elif res in "NO No no N n":
        print("\nThank you for visiting Kitchen Connections.")
    else:
        print("\nAn invalid choice is entered.")
        sys.exit()

