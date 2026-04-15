#Using import random for generating a random seat number in the Cruise Ship.
import random

#Using import time to give time duration for print statements.
import time
     
#Using import sys to exit program if user enters an invalid choice
import sys

#Using import csv to create table
import csv

#Below imported modules contain def functions and print statements for the Source Code
import bookerrors
import roomerrors
import roombkerrors
import OCRiveria
import Arcrink
import allres
import med
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
import Reserrors
import msgerrors
import msgtimerrors
import spaerrors
import RG
import NSG
import arcerrors
import waterpkerrors
import sporterrors
import idgameserrors
import Fic            
import NonF
import Nov
import Mys
import Poe
import HisFan
import YAF
import His
import SS
import Fan
import GN
import AdFic
import FT
import CLit
import ConLit
import CriFic
import Comic
import NAF
import Spir
import Phil
import liberrors
import amenerrors
import facerrors   


#Booking a seat in the Cruise Ship
def bookin():
    global name
    global lname
    global adree
    print("\n\t\t\tWelcome to Costa Cruises Ship booking system")
    print("")#This is being used in order to separate multiple lines using whitespaces.
    name=input("Please enter first name:")
    lname=input("Please enter last name:")
    adree=input("Please enter address :")
    phno=int(input("Please enter phone number:"))
    print("\n")
bookin()



#Confirmation of a destination
def book ():
    global destination
    global price
    f=open("bookintext.txt",'r')
    d=f.read()
    print(d)
    dest=int(input("\nPlease enter required choice from the above options(1/2/3):"))
    price=0
    
    if dest==1:
        destination="Egypt,Jordan and Oman"
        price=10200
    elif dest==2:
        destination="Seychelles,Kenya and Tanzania"
        price=25600       
    elif dest==3:
        destination='Madagascar'
        price=15500
    else:
        print("""\nAn invalid choice is entered.
    Please enter a valid choice.""")
        print("")#This is being used in order to separate multiple lines using whitespaces.
        bookerrors.bookerr()
book()



#What type of suite does the user require?   
print("\n1.)Regular suite-1,200 AED \n2.)Premium suite-3,000 AED")

cruisetype=int(input("Please enter room you prefer(1/2):"))
roomtype=" "

if cruisetype==1:
    roomtype='Premium suite'
    price+=3000
    print("Your ticket has been booked!")
    roomno=random.randint(1,500)
elif cruisetype==2:
     roomtype='Regular suite'
     price+=1200
     print("Your ticket has been booked!")
     roomno=random.randint(1,500)

else:
    print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
    #Giving user a second attempt to enter a valid choice
    print("")
    roomerrors.roomerr()    

        
    
#Review booking.
q=input("\nDo you want to review your booking?(Yes/No):")
print("")
try:
    if q in "YES Yes yes Y y":
        print("Name:",name,lname)
        print("Address:",adree)
        print("Cruise destination:",destination)
        print("Suite:",roomtype)
        print("Total price:",price)
        print("Room number:",roomno)
        time.sleep(2)
        print("""\nThank you for booking the Costa Cruise. Have a wonderful stay!
The Concierge will guide you to you room. """)
    elif q in "NO No no N n":
        print("""Thank you for booking the Costa Cruise. Have a wonderful stay!
The Concierge will guide you to you room. """)  
except:
    print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
    sys.exit()        

#Creating table for Room Booking Reservation 
a=open("room_booking.csv",'a')
A=csv.writer(a)
A.writerow([name,lname,adree,destination,roomtype,price,roomno])
a.close()

#Room Reservation
def roombooking():
    time.sleep(2)
    print("""\n \tRoom Reservation
Press 1 to book seat in first floor 
Press 2 to book seat in second floor 
Press 3 to book seat in third floor
Maximum capacity is 5 people \n""")
    room_a = []
    room_b = []
    room_c = []
    choice = int(input("Please enter a valid choice(1/2/3):")) 
    check = True
    while check == True:
        number = int(input("Enter for how many people is the room reserved for:"))
        if number > 5:
            print("Too many people")
        else:
            check = False
    
    if choice == 1 :
        for i in range (0,number):
            x = input("Enter visitor's name:")
            print("")
            room_a.append(x)
    elif choice == 2:
        for i in range (0,number):
            x = input("Enter visitor's name:")
            print("")
            room_b.append(x)
    elif choice == 3:
        for i in range (0,number):
            x = input("Enter visitor's name:")
            print("")
            room_c.append(x)
    else:
        print("""\nAn invalid choice is entered.
    Please enter a valid choice given from the above options.""")
        #Giving user a second attempt to enter a valid choice
        print("")
        roombkerrors.roombkerr()
roombooking()



#Reception providing information about the Cruise Ship
def reception():
    f=open("receptiontext.txt",'r')
    d=f.read()
    loop="Yes"
    while loop=="Yes":
        print(d)
        qwchoice=int(input("\nPlease enter a valid choice(1/2/3/4):"))
        print("")
        if qwchoice==1:
            OCRiveria.OC()
            time.sleep(2)   
        elif qwchoice==2:
            Arcrink.arcrink()
            time.sleep(2)
        elif qwchoice==3:
            allres.Allres()
            time.sleep(2)    
        elif qwchoice==4:
            med.Med()
            time.sleep(2)
            
        loop=input("\nWould you like to go through our reception center once more?(Yes/No):")
        print("")
        if loop=="NO No no N n":
            break     
reception() 


time.sleep(2)
#Facilities provided by Cruise Ship       
def facilities():
    print("")
    f=open("factext.txt",'r')
    d=f.read()
    print(d)
    print("")
    
CHOICE="y"

while CHOICE in "YES Yes yes Y y":
    if CHOICE in "YES Yes yes Y y":
        facilities()
        choice=int(input("Please enter a valid choice(1/2/3):"))

        try:
            if choice==1:
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
1.)8:00-11:30 --->  Breakfast
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
                    print("""An invalid choice is entered.
Please enter a valid choice given from the above options.""")
                    #Giving user a second attempt to enter a valid choice
                    print("")
                    Reserrors.reserr()
                        
                if opt in "NONonoNn":
                    print("Thank you for visiting dining experiences, have a great day!")


                
            if choice==2:
                print("""\n\t\tOnboard Entertainment
Sail better with up to 6,500 channels on our award-winning onboard
entertainment system.Choose from up to 6,500 channels of movies, 
TV shows, music and games, on demand and in 
multiple languages.""")
            

            
            if choice==3:
                print("""\nBelow are the amenities that the cruise ship provides:
1.)Pools and Sundecks
2.)Spa
3.)Fitness Center
4.)Arcade
5.)Water park
6.)Football ground,Basketball Court,Tennis courts
7.)Billiards,Carrom,Chess
8.)Library
9.)Ice skating rink
10.)Children's Play Area""")
                
                time.sleep(2)
                opt=int(input("\nPlease enter a valid choice(1/2/3/4/5/6/7/8/9/10):"))
                print("")
                
                try:
                    if opt==1:
                        def pools():
                            f=open("poolstext.txt",'r')
                            d=f.read()
                            print(d)
                        pools()
                    
                    elif opt==2:
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
                            print("""\nVarious types of messages that are provided
1)Head Massage
2)Back & Shoulders Massage
3)Deep Tissue Massage
4)Hot stone Massages""")
                            msg=int(input("Please enter a valid choice(1/2/3/4):"))
                            m=""
                            if msg==1:
                                d="Head massage "
                                m=m+d
                            elif msg==2:
                                d="Back and Shoulders massage "
                                m=m+d
                            elif msg==3:
                                d="Deep tissue massage "
                                m=m+d
                            elif msg==4:
                                d="Hot stone massage "
                                m=m+d
                            else:
                                print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                                #Giving user a second attempt to enter a valid choice
                                print("")
                                msgerrors.msgerr()
                            print("""\nTime slots that are provided
1)8:00-10:00 ---> Morning
2)13:00-15:00 ---> Afternoon 
3)17:00-18:00 ---> Evening""")
                            timing=int(input("Please enter a valid choice(1/2/3):"))
                            t=""
                            if timing==1:
                                tim="8:00-10:00 ---> Morning "
                                t=t+tim
                            elif timing==2:
                                tim="13:00-15:00 ---> Afternoon "
                                t=t+tim
                            elif timing==3:
                                tim="17:00-18:00 ---> Evening "
                                t=t+tim
                            else:
                                print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                                #Giving user a second attempt to enter a valid choice
                                print("")
                                msgtimerrors.msgtimerr()
                            q2=name+":"+m+","+"at"+t
                            s.write(q2)
                            s.close()
                            print("Alright ",name," you have booked for a ",m,"at",t)
                            print(""" We look forward for having you to our spa.
Have a nice day""")
                            
                        elif ch in "NO No no N n":
                            print("\nThank you for visiting the spa.")

                        else:
                             print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                            #Giving user a second attempt to enter a valid choice
                             print("")
                             spaerrors.spaerr()

                        #Creating table for SPA Reservation
                        c=open("spa_booking.csv",'a')
                        C=csv.writer(c)
                        C.writerow([name,m,t])
                        c.close()
                            
                    elif opt==3:
                        def fit():
                            f=open("fittext.txt",'r')
                            d=f.read()
                            print(d)
                        fit()
                        name=input("\nPlease enter the name you have used to book your cruise:")
                        sno=int(input("Please enter the room number:"))
                        if sno>500:
                            print("Please check your room number and try again.")
                        else:
                            pass
                    
                    elif opt==4:
                        def arc():
                            f=open("arctext.txt",'r')
                            d=f.read()
                            print(d)
                        arc()
                        print("")
                        ch=int(input("Please enter a valid choice(1/2):"))
                        print("")
                        if ch==1:
                            RG.rg()
                        elif ch==2:
                            NSG.nsg()
                        else:
                            print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                            #Giving user a second attempt to enter a valid choice
                            print("")
                            arcerrors.arcerr()
                        
            
                    elif opt==5:
                        print("""Settle aboard a gleaming yacht with sunbathing and seating decks,
and absorb the landmarks as you glide over""")
                        q=input("\nWould you like to book a ticket for waterpark?(Yes/No):")
                        if q in "Yes YES yes Y y":
                            n=int(input("How many tickets would you like to book?:"))
                            waterpark=[]
                            for i in range(n):   
                                name=input("Enter name of visitor:")
                                waterpark.append(name)
                            print("""Please feel free to visit the waterpark
from 10am-8pm.
Thank you for visiting the waterpark """)
                        elif q in "NO No no N n":
                            print("""Thank you for visiting the waterpark.
Have a good day.""")
                        else:
                            print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                            #Giving user a second attempt to enter a valid choice
                            print("")
                            waterpkerrors.waterpkerr() 

                            

                    elif opt==6:
                            print("""We have 8 Tennis courts ,4 Basketball
courts and 2 Football grounds""")
                            q=input("\nWould you like to book any court?(Yes/No):")
                            if q in "Yes YES yes Y y":
                                spo=[]
                                print("""Below are the time slots that are provided:
1.)8:00-10:00
2.)12:00-14:00
3.)16:00-18:00""")                                
                                sporttimings=input("Please enter a required time slot:")
                                sports=input("Please enter a sport:")

                                def sporttims(): 
                                    global sporttimings
                                    global sports
                                    
                                    if sporttimings not in "8:00-10:00 12:00-14:00 16:00-18:00":
                                        print("")
                                        print("An invalid choice is entered for time slot.")
                                        sporttimings=input("Please enter a valid time slot:")
                                        
                                    if sports not in "Tennis Basketball Football":
                                        print("An invalid choice is entered for the choice of games.")
                                        sports=input("Please enter a specified indoor game:")
                                
                                sporttims()
                                print("Alright,",sports,"court has been booked between",sporttimings)
                                spo.append(sports)
                                spo.append(sporttimings)

                                #Creating table for Sports Reservation
                                d=open("sports_booking.csv",'a')
                                D=csv.writer(d)
                                D.writerow([name,sports,sporttimings])
                                d.close()
                                
                            elif q in "NO No no N n":
                                print("Thank you for visiting!")

                            else:
                                print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                                #Giving user a second attempt to enter a valid choice
                                print("")
                                sporterrors.sporterr()



                    elif opt==7:
                        print("""The indoor games that are provided:
1)Billiards
2)Carrom
3)Chess""")
                        q=input("\nWould you like to play any indoorgame?(Yes/No):")

                        if q in "YES Yes yes Y y":
                            indoorgamelist=[]
                            print("""\nBelow are the time slots that are provided:
1.)8:00-10:00
2.)12:00-14:00
3.)16:00-18:00""")
                            name=input("Please enter a valid name:")
                            Idgstimings=input("Please enter a required time slot:")
                            Indoorgames=input("Please enter an indoor game(Billiards/Carrom/Chess):")
                            indoorgamelist.append([name,Idgstimings,Indoorgames])

                            def idgametimg(): 
                                global Idgstimings
                                global Indoorgames
                                
                                if Idgstimings not in "8:00-10:00 12:00-14:00 16:00-18:00":
                                    print("")
                                    print("An invalid choice is entered for time slot.")
                                    Idgstimings=input("Please enter a valid time slot:")
                                    
                                if Indoorgames not in "Billiards Carrom Chess":
                                    print("An invalid choice is entered for the choice of games.")
                                    Indoorgames=input("Please enter a specified indoor game:")
                            
                            idgametimg()  
                            print("Alright,",Indoorgames,"indoor game has been booked for",Idgstimings)
                            indoorgamelist.append(Indoorgames)
                            indoorgamelist.append(Idgstimings)

                            #Creating table for Indoor games Reservation
                            d=open("indoorgames_booking.csv",'a')
                            D=csv.writer(d)
                            D.writerow([name,Indoorgames,Idgstimings])
                            d.close()
                            
                        elif q in "NO No no N n":
                            print("Thank you for visiting!")

                        else:
                            print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                            #Giving user a second attempt to enter a valid choice
                            print("")
                            idgameserrors.idgameserr()



                    elif opt==8:
                        def lib():
                            f=open("libtext.txt",'r')
                            d=f.read()
                            print(d)
                        lib()
                        ch=int(input("Please enter a valid choice from choice 1 to choice 20:"))
                        print("")
                        if ch==1:
                            Fic.fic()
                        elif ch==2:
                            NonF.nonf()
                        elif ch==3:
                            Nov.nov()
                        elif ch==4:
                            Mys.mys()
                        elif ch==5:
                            Poe.poe()
                        elif ch==6:
                            HisFan.hisfan()
                        elif ch==7:
                            YAF.yaf()
                        elif ch==8:
                            His.his()
                        elif ch==9:
                            SS.ss()
                        elif ch==10:
                            Fan.fan()
                        elif ch==11:
                            GN.gn()
                        elif ch==12:
                            AdFic.adfic()
                        elif ch==13:
                            FT.ft()
                        elif ch==14:
                            CLit.clit()
                        elif ch==15:
                            ConLit.conlit()
                        elif ch==16:
                            CriFic.crific()
                        elif ch==17:
                            Comic.comic()
                        elif ch==18:
                            NAF.naf()
                        elif ch==19:
                            Spir.spir()
                        elif ch==20:
                            Phil.phil()
                        else:
                            print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                            #Giving user a second attempt to enter a valid choice
                            print("") 
                            liberrors.liberr()


                    elif opt==9:
                        name=input("Please enter a valid name:")
                        iceskating=[]
                        iceskating.append(name)
                        print("""Your name has been registered for the ice rink at
                        3 pm to 9 pm daily.Have Fun!""")
                        
                    elif opt==10:
                        def cpa():
                            f=open("cpatext.txt",'r')
                            d=f.read()
                            print(d)
                        cpa()
                    
                except:
                    print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
                    #Giving user a second attempt to enter a valid choice
                    print("")
                    amenerrors.amenerr()

        except:
            print("""\nAn invalid choice is entered.
Please enter a valid choice given from the above options.""")
            #Giving user a second attempt to enter a valid choice
            print("")
            facerrors.facerr()
    
    CHOICE=input("\nWould you like to go through our facilities again?(Yes/No):")
    
    print("")
    if CHOICE in "NONonoNn":
        print("""\nThank you for checking out the facilities that we provide on th cruise ship.
Have a wonderful day""")
        cho="y"    
        while cho in "YESYesyesYy":
            if cho in "YESYesyesYy":
                print("""\nWhich of the following bookings would you like to go through
1.)Room
2.)Restaurant
3.)Spa
4.)Sports
5.)Indoor games""")
        
                CH=int(input("\nEnter a valid choice(1/2/3/4/5):"))
                
                if CH==1:
                    with open("room_booking.csv",'r',newline="\r\n") as a:
                        A=csv.reader(a, delimiter='|')
                        for i in A:
                            print(i)

                if CH==2:
                    print("""The below restaurant provide booking services
1.)Nuska Restaurant
2.)Bastion Restaurant
3.)DandC Restaurant
4.)KC Restaurant
5.)Fika Restaurant
6.)Murray's Restaurant""")
                    choice=input("Which restaurant booking service would you to view(1/2/3/4/5/6):")
                    if choice==1:
                            with open('nuskarest_booking.csv','r',newline="\r\n") as b:
                                    B=csv.reader(b, delimiter='|')
                                    for i in B:
                                        print(i)
                    if choice==2:
                            with open('bastionrest_booking.csv','r',newline="\r\n") as b:
                                    B=csv.reader(b, delimiter='|')
                                    for i in B:
                                        print(i)
                    if choice==3:
                            with open('dandcrest_booking.csv','r',newline="\r\n") as b:
                                    B=csv.reader(b, delimiter='|')
                                    for i in B:
                                        print(i)
                    if choice==4:
                            with open('kcrest_booking.csv','r',newline="\r\n") as b:
                                    B=csv.reader(b, delimiter='|')
                                    for i in B:
                                        print(i)
                    if choice==5:
                            with open('fikarest_booking.csv','r',newline="\r\n") as b:
                                    B=csv.reader(b, delimiter='|')
                                    for i in B:
                                        print(i)
                    if choice==6:
                            with open('murraysrest_booking.csv','r',newline="\r\n") as b:
                                    B=csv.reader(b, delimiter='|')
                                    for i in B:
                                        print(i)


                if CH==3:
                    with open('spa_booking.csv','r',newline="\r\n") as c:
                        C=csv.reader(c, delimiter='|')
                        for i in C:
                            print(i)

                if CH==4:
                    with open('sports_booking.csv','r',newline="\r\n") as d:
                        D=csv.reader(d, delimiter='|')
                        for i in D:
                            print(i)

                if CH==5:
                    with open('indoorgames_booking.csv','r',newline="\r\n") as d:
                        D=csv.reader(d, delimiter='|')
                        for i in D:
                            print(i)

            cho=input("\nWould you like to go through the booking system again?(Yes/No):")

            if cho in "NO No no N n":
                print("\nThank you for booking with Costa Cruise Ship.")
                                                                                                                                                                                                                                
