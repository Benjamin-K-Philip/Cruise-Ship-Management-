#sporterrors
import sys
def sporterr():
    print("""We have 8 Tennis courts ,4 Basketball
courts and 2 Football grounds""")
    q=input("Would you like to book any court?(Yes/No)")
    if q in "YES Yes yes Y y":
        sport=[]
        print(""" Below are the time slots that are provided:
                     1.)8:00-10:00
                     2.)12:00-14:00
                     3.)16:00-18:00
                     """)
        time=input("Please enter a required time slot:")
        sports=input("Please enter a sport:")
        print("Alright,",sports,"court has been booked")
        sport.append(sports)
        sport.append(time)
        def sporttims(): #rq means required sport
            global time
            global sports
            
            if time not in "8:00-10:00 12:00-14:00 16:00-18:00":
                print("")
                print("An invalid choice is entered for time slot.")
                time=input("Please enter a valid time slot:")
                
            if sports not in "Tennis Basketball Football":
                print("An invalid choice is entered for the choice of games.")
                sports=input("Please enter a specified indoor game:")
        
        sporttims()
        print("Alright,",sports,"indoor game has been booked at ",time,".")
        spo.append(sports)
        spo.append(time)
    elif q in "NO No no N n":
        print("Thank you for visiting!")

    else:
        print("An invalid choice is entered")
        sys.exit()

