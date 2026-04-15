#fikatimeerrors
import sys
def fikatimerr():
    print("""Below are the time slots provided for dining in 
1.)12:00-16:00 ---> Lunch
2.)18:00-22:00 ---> Dinner""")
    time=int(input("What time would you like to dine with us?(1/2):"))
    t=""
    if time==1:
        tim="12:00-16:00 ---> Lunch"
        t=t+tim
    elif time==2:
        tim="18:00-22:00 ---> Dinner"
        t=t+tim
    else:
        print("An invalid choice is entered.")
        sys.exit()
