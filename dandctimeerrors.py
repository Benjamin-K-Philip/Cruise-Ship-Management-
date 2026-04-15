#dandctimeerrors
import sys
def dandctimerr():
    print("""Below are the time slots provided for dining in 
1.)12:00-16:00 ---> Lunch
2.)19:00-00:00 ---> Dinner and Bar""")
    time=int(input("What time would you like to dine with us?(1/2):"))
    t=""
    if time==1:
        tim="12:00-16:00 ---> Lunch"
        t=t+tim
    elif time==2:
        tim="19:00-00:00 ---> Dinner and Bar"
        t=t+tim
    else:
        print("An invalid choice is entered.")
        sys.exit()


