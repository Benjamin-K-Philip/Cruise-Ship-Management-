#dandcerrors
import sys
import dandctimeerrors
def dandcerr():
    f=open("DandCtext.txt",'r')
    d=f.read()
    print("")
    name=input("Please enter a valid name:")
    res=input("\nWould you like to book a table at our restaurant?(Yes/No):")
    if res in "YES Yes yes Y y":
        Dandcc=open('Dandc.txt','a+')
        table=int(input("\nHow many guests are we expecting?:"))
        print("""Below are the time slots provided for dining in 
    1.)12:00-16:00 ---> Lunch
    2.)19:00-00:00 ---> Dinner and Bar""")
        time=int(input("What time would you like to dine with us?(1/2):"))
        t=""
        if time==1:
            tim="12:00-16:00 ---> Lunch "
            t=t+tim
        elif time==2:
            tim="19:00-00:00 ---> Dinner and Bar "
            t=t+tim
        else:
            print("""\nAn invalid choice is entered.
    Please enter a valid choice given from the above options.""")
            #Giving user a second attempt to enter a valid choice
            print("")
            dandctimeerrors.dandctimerr()   
        print("\nAlright,",name,"table for",table,"is reserved for,",t)
        a=name+','+str(table)+','+ t
        Dandcc.write(a)
        Dandcc.close()
        print("""We look forward to giving you the best dining experience.
Have a great day!""")
    elif res in "NO No no N n":
       print("\nThank you for visiting Dhow and Anchor.")
    else:
        print("\nAn invalid choice is entered.")
        exit()
