#spaerrors
import sys
import msgerrors
import msgtimerrors
def spaerr():
    def spa():
        f=open("spatext.txt",'r')
        d=f.read()
        print(d)
    spa()
    print("")
    ch=input("Would you like to book at any of our spas?(Yes/No):")
    if ch in "YES Yes yes Y y":
        s=open('spa.txt','a+')
        name=input("Please enter your name:")
        print("""\n Various types of messages that are provided
1)Head Massage
2)Back & Shoulders Massage
3)Deep Tissue Massage
4)Hot stone Massages""")
        msg=int(input("Please enter a valid choice(1/2/3/4):"))
        m=""
        try:
            if msg==1:
                d="Head massage"
                m=m+d
            elif msg==2:
                d="Back and Shoulders massage"
                m=m+d
            elif msg==3:
                d="Deep tissue massage"
                m=m+d
            elif msg==4:
                d="Hot stone massage"
                m=m+d
        except:
            print("""\nAn invalid choice is entered.
        Please enter a valid choice given from the above options.""")
            #Giving user a second attempt to enter a valid choice
            msgerrors.msgerr()
        print("""\nTime slots that are provided
1)Morning:- 8:00-10:00
2)Afternoon:- 1:00-3:00
3)Evening:- 5:00-6:00""")
        timing=int(input("Please enter a valid choice(1/2/3):"))
        t=""
    
        if timing==1:
            tim="Morning 8:00-10:00"
            t=t+tim
        elif timing==2:
            tim=" Afternoon 1:00-3:00"
            t=t+tim
        elif timing==3:
            tim="Evening 5:00-6:00"
            t=t+tim
        else:
            print("""\nAn invalid choice is entered.
        Please enter a valid choice given from the above options.""")
            #Giving user a second attempt to enter a valid choice
            msgtimeerrors.msgtimerr()
        q2=name+":"+m+","+"at"+t
        s.write(q2)
        s.close()
        print("Alright",name,"you have booked for a",m,"at",t,".")
        print("""We look forward for having you to our spa.
Have a nice day""")
        
    elif ch in "NO No no N n":
        print("Thank you for visiting the spa.")

    else:
        print("An invalid choice is entered.")
        sys.exit()

    
