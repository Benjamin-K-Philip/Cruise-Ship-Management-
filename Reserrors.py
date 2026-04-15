#Reserrors
import time
import sys
import nuskatimeerrors
import nuskaerrors
import bastiontimeerrors
import bastionerrors
import dandctimeerrors
import dandcerrors
import kctimeerrors
import kcerrors
import ccerrors
import fikatimeerrors
import fikaerrors
import f24errors
import murraystimeerrors
import murrayserrors
import IVM
import NVHM
import VJM
import KM
import BM                              
import DM
import GFM
import LFM
import LSM
import LLM
import Rmealserrors
import MDieterrors
import BabyM
import CM
import bmealserrors
import SMerrors
def reserr():
    print("""\nSignature dining for all occasions that are provided
            1.)Nuska Beach
            2.)Bastion
            3.)Dhow and Anchor
            4.)Kitchen Connections
            5.)Creations Cakery
            6.)Fika
            7.)Floor 24
            8.)Murray's
            9.)Special Meals""")
    time.sleep(3)
                
    opt=input("Would you like to know more about the given restaurants?(Yes/No):")

    try:
        if opt in "YES Yes yes Y y":
            print("")
            resch=int(input("Please enter a valid choice(1/2/3/4/5/6/7/8/9):"))
            print("")
            
            if resch==1:
                def nuska():
                    f=open("nuskatext.txt",'r')
                    d=f.read()
                    print(d)
                nuska()
                print("")
                res=input("\nWould you like to book a table at our restaurant?(Yes/No):")
                if res in "YES Yes yes Y y":
                    nuska=open('nuska.txt','a+')
                    table=int(input("\nHow many guests are we expecting?:"))
                    print("""Below are the time slots provided for dining in 
                1.)8:00 -11:30 --->  Breakfast
                2.)11:30-13:00 --->  Brunch
                3.)13:00-16:00 --->  Lunch
                4.)16:00-18:00 --->  Refreshments
                5.)18:00-23:00 --->  Dinner""")        
                    timeslot=int(input("Enter a valid time slot(1/2/3/4/5):"))
                    t=""
                    if timeslot==1:
                        tim="8:00 -11:30 ---> Breakfast "
                        t=t+tim
                    elif timeslot==2:
                        tim="11:30-13:00 --->  Brunch "
                        t=t+tim
                    elif timeslot==3:
                        tim="13:00-16:00 --->  Lunch "
                        t=t+tim
                    elif timeslot==4:
                        tim="16:00-18:00 --->  Refreshments "
                        t=t+tim
                    elif timeslot==5:
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
                    print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                    #Giving user a second attempt to enter a valid choice
                    print("")
                    nuskaerrors.nuskaerr()
                
                #Creating table for Restaurant Nuska Reservation
                b=open("nuskarest_booking.csv",'a')
                B=csv.writer(b)
                B.writerow([name,table,t])
                b.close()                                

            elif resch==2:
                def bastion():
                     f=open("bastiontext.txt",'r')
                     d=f.read()
                     print(d)
                bastion()
                print("")
                res=input("\nWould you like to book a table at our restaurant?(Yes/No):")
                if res in "YES Yes yes Y y":
                    bastion=open('bastion.txt','a+')
                    table=int(input("\nHow many guests are we expecting?:"))
                    print("""Below are the time slots provided for dining in 
                1.)12:30-15:00 ---> Lunch
                2.)18:00-23:00 ---> Dinner and Bar""")
                    timeslot=int(input("What time would you like to dine with us?(1/2):"))
                    t=""
                    if timeslot==1:
                        tim="12:30-15:00 ---> Lunch "
                        t=t+tim
                    elif timeslot==2:
                        tim="18:00-23:00 ---> Dinner and Bar "
                        t=t+tim
                    else:
                        print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                        #Giving user a second attempt to enter a valid choice
                        print("")
                        bastiontimeerrors.bastiontimerr()
                    print("\nAlright,",name,"table for",table,"is reserved for,",t)
                    a=name+','+str(table)+','+t 
                    bastion.write(a)
                    bastion.close()
                    print("""We look forward to giving you the best dining experience.
Have a great day!""")
                    pass
                elif res in "NO No no N n":
                    print("\nThank you for visiting Bastion.")
                else:
                    print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                    #Giving user a second attempt to enter a valid choice
                    print("")
                    bastionerrors.bastionerr()
                #Creating table for Restaurant Bastion Reservation
                b=open("bastionrest_booking.csv",'a')
                B=csv.writer(b)
                B.writerow([name,table,t])
                b.close()                            

            elif resch==3:
                def DandC():
                     f=open("DandCtext.txt",'r')
                     d=f.read()
                     print(d)
                DandC()
                print("")
                res=input("\nWould you like to book a table at our restaurant?(Yes/No):")
                if res in "YES Yes yes Y y":
                    Dandcc=open('Dandc.txt','a+')
                    table=int(input("\nHow many guests are we expecting?:"))
                    print("""Below are the time slots provided for dining in 
                1.)12:00-16:00 ---> Lunch
                2.)19:00-00:00 ---> Dinner and Bar""")
                    timeslot=int(input("What time would you like to dine with us?(1/2):"))
                    t=""
                    if timeslot==1:
                        tim="12:00-16:00 ---> Lunch "
                        t=t+tim
                    elif timeslot==2:
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
                    DandC.write(a)
                    DandC.close()
                    print("""We look forward to giving you the best dining experience.
Have a great day!""")
                elif res in "NO No no N n":
                   print("\nThank you for visiting Dhow and Anchor.")
                else:
                    print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                    #Giving user a second attempt to enter a valid choice
                    print("")
                    dandcerrors.dandcerr()
                
                #Creating table for Restaurant DandC Reservation
                b=open("dandcrest_booking.csv",'a')
                B=csv.writer(b)
                B.writerow([name,table,t])
                b.close()

            elif resch==4:
                def KC():
                     f=open("KCtext.txt",'r')
                     d=f.read()
                     print(d)
                KC()
                print("")
                res=input("\nWould you like to book a table at our restaurant?(Yes/No):")
                if res in "YES Yes yes Y y":
                    Kc=open('KC.txt','a+')
                    table=int(input("\nHow many guests are we expecting?:"))
                    print("""Below are the time slots provided for dining in 
                1.)07:00-11:00 ---> Breakfast
                2.)18:00-23:00 ---> Dinner""")
                    timeslot=int(input("What time would you like to dine with us?(1/2):"))
                    t=""
                    if timeslot==1:
                        tim="07:00-11:00 ---> Breakfast "
                        t=t+tim
                    elif timeslot==2:
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
                    print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                    #Giving user a second attempt to enter a valid choice
                    print("")
                    kcerrors.kcerr()

                #Creating table for Restaurant KC Reservation
                b=open("kcrest_booking.csv",'a')
                B=csv.writer(b)
                B.writerow([name,table,t])
                b.close()

            elif resch==5:
                def cc():
                    f=open("cctext.txt",'r')
                    d=f.read()
                    print(d)
                cc()
                print("")
                res=input("\nWould you like to book a table at our bakery?(Yes/No):")
                if res in "YES Yes yes Y y":
                    a=name
                    cc.write(a)
                    cc.close()
                    print("""We look forward to giving you the best dining experience.
Have a great day!""")
                elif res in "NO No no N n":
                       print("\nThank you for visiting Creations Cakery.")
                else:
                    print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                    #Giving user a second attempt to enter a valid choice
                    print("")
                    ccerrors.ccerr()


            elif resch==6:
                def fika():
                     f=open("fikatext.txt",'r')
                     d=f.read()
                     print(d)
                fika()
                print("")
                res=input("\nWould you like to book a table at our restaurant?(Yes/No):")
                if res in "YES Yes yes Y y":
                    fika=open('fika.txt','a+')
                    table=int(input("\nHow many guests are we expecting?:"))
                    print("""Below are the time slots provided for dining in 
                1.)12:00-16:00 ---> Lunch
                2.)18:00-22:00 ---> Dinner""")
                    timeslot=int(input("What time would you like to dine with us?(1/2):"))
                    t=""
                    if timeslot==1:
                        tim="12:00-16:00 ---> Lunch "
                        t=t+tim
                    elif timeslot==2:
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
                    print("""\nWe look forward to giving you the best dining experience.
Have a great day!""")
                elif res in "NO No no N n":
                    print("\nThank you for visiting Fika.")
                else:
                    print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                    #Giving user a second attempt to enter a valid choice
                    print("")
                    fikaerrors.fikaerr()

                #Creating table for Restaurant Fika Reservation
                b=open("fikarest_booking.csv",'a')
                B=csv.writer(b)
                B.writerow([name,table,t])
                b.close()
                    

            elif resch==7:
                def f24():
                    f=open("f24text.txt",'r')
                    d=f.read()
                    print(d)
                f24()
                print("")
                res=input("\nWould you like to book a table at our restaurant?(Yes/No):")
                if res in "YES Yes yes Y y":
                    a=name
                    f24.write(a)
                    f24.close()
                    print("""\nWe look forward to giving you the best dining experience.
Have a great day!""")
                elif res in "NO No no N n":
                    print("\nThank you for visiting Floor 24.")
                else:
                    print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                    #Giving user a second attempt to enter a valid choice
                    print("")
                    f24errors.f24err()


            elif resch==8:
                def murrays():
                    f=open("murraystext.txt",'r')
                    d=f.read()
                    print(d)
                murrays()
                print("")
                res=input("\nWould you like to book a table at our restaurant?(Yes/No):")
                if res in "YES Yes yes Y y":
                    murrays=open('murrays.txt','a+')
                    name=input("Please enter a desired name in order to book a table:")
                    table=int(input("How many guests are we expecting?:"))
                    print("""Below are the time slots provided for dining in 
                1.)12:00-16:00 ---> Lunch
                2.)18:00-22:00 ---> Dinner""")
                    timeslot=int(input("What time would you like to dine with us?(1/2):"))
                    t=""
                    if timeslot==1: 
                        tim="12:00-16:00 ---> Lunch "
                        t=t+tim
                    elif timeslot==2:
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
                    print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                    #Giving user a second attempt to enter a valid choice
                    print("")
                    murrayserrors.murrayserr()

                #Creating table for Restaurant Murray's Reservation
                b=open("murraysrest_booking.csv",'a')
                B=csv.writer(b)
                B.writerow([name,table,t])
                b.close()
                    

            elif resch==9:
                def SM():
                     f=open("SMtext.txt",'r')
                     d=f.read()
                     print(d)
                SM()

                SMcho=int(input("Please enter a valid(1/2/3/4):"))

                if SMcho==1:
                    def Rmeals():
                        print("""1.)Indian Vegeterian Meal
                    2.)Non-Vegeterian Hindu Meal
                    3.)Vegterian Jain Meal
                    4.)Kosher Meal""")    
                        ch=int(input("Which meal option you would like to view?:"))
                        if ch==1:
                            IVM.ivm()
                        elif ch==2:
                            NVHM.nvhm()
                        elif ch==3:
                            VJM.vjm()
                        elif ch==4:
                            KM.km()
                        else:
                            print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""") 
                            #Giving user a second attempt to enter a valid choice
                            print("")
                            Rmealserrors.Rmealserr() 
                    Rmeals()

                elif SMcho==2:
                    def MedDiet():
                        f=open("MedDiet()text.txt",'r')
                        d=f.read()
                        print(d)
                    MedDiet()
                    ch=int(input("Which meal option would you like to view?(1 to 6):"))
                    if ch==1:
                        BM.bm()
                    elif ch==2:
                        DM.dm()
                    elif ch==3:
                        GFM.gfm()
                    elif ch==4:
                        LFM.lfm()
                    elif ch==5:
                        LSM.lsm()
                    elif ch==6:
                        LLM.llm()
                    else:
                        print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""") 
                        #Giving user a second attempt to enter a valid choice
                        print("")
                        MDieterrors.mdieterr()                                         

                elif SMcho==3:
                    def Vegan():
                         f=open("Vegantext.txt",'r')
                         d=f.read()
                         print(d)
                    Vegan()

                elif SMcho==4:
                    def babymeals():
                        print("1.)Baby Meals \n2.)Child Meals")
                        opt=int(input("Which meal would you like to view?(1/2):"))
                        if opt==1:
                            BabyM.babym()
                        elif opt==2:
                            CM.cm()
                        else:
                            print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""") 
                        #Giving user a second attempt to enter a valid choice
                            print("")
                            bmealserrors.bmealserr() 
                    babymeals()

                else:
                    print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                    #Giving user a second attempt to enter a valid choice
                    print("")
                    SMerrors.smerr()
    except:
        print("An invalid choice is entered.")
        sys.exit()

