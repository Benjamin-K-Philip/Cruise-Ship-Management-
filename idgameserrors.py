#idgameserrors
import sys
def idgameserr():
    print("""The indoor games that are provided:
1)Billiards
2)Carrom
3)Chess""")
    q=input("\nWould you like to play any indoorgames?(Yes/No):")

    if q in "YES Yes yes Y y":
        indoorgamelist=[]
        print("""\nBelow are the time slots that are provided:
                     1.)8:00-10:00
                     2.)12:00-14:00
                     3.)16:00-18:00
                     """)
        name=input("Please enter a valid name:")
        time=input("Please enter a required time slot:")
        Indoorgames=input("Please enter an indoor game(Billiards/Carrom/Chess):")
        indoorgamelist.append([name,time,Indoorgames])

        def idgametimg():
            global time
            global Indoorgames
            
            if time not in "1 2 3":
                print("")
                print("An invalid choice is entered for the choice of time slot.")
                time=input("Please enter a valid time slot:")
                
            if Indoorgames not in "Billiards Carrom Chess":
                print("An invalid choice is entered for the choice of games.")
                Indoorgames=input("Please enter a specified indoor game:")
        
        idgametimg()  
        print("Alright,",Indoorgames,"indoor game has been booked.")
        indoorgamelist.append(Indoorgames)
        indoorgamelist.append(time)
        
    if q in "NO No no N n":
        print("Thank you for visiting!")

    if q not in "YES Yes yes Y y NO No no N n":
        print("An invalid choice is entered")
        sys.exit()

