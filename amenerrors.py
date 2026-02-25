#amenerrors
import time
import sys
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
def amenerr():
    print(""" \nBelow are the amenities that the cruise ship provides:
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
        C.writerow([name,table,t])
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
        print("")
        q=input("Would you like to book a ticket for waterpark?(Yes/No):")
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
             3.)16:00-18:00
             """)
                
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
                
                
                print("Alright,",sports,"court has been booked between",sporttimings)
                spo.append(sports)
                spo.append(sporttimings)
                
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
                         3.)16:00-18:00
                         """)
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

    else:
        print("An invalid choice is entered.")
        sys.exit()

