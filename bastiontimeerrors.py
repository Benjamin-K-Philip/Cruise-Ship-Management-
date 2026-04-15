#bastiontimeerrors
import sys
def bastiontimerr():
    print("""Below are the time slots provided for dining in 
1.)12:30-15:00 ---> Lunch
2.)18:00-23:00 ---> Dinner and Bar""")
    time=int(input("What time would you like to dine with us?(1/2):"))
    t=""
    if time==1:
        tim="12:30-15:00 ---> Lunch "
        t=t+tim
    elif time==2:
        tim="18:00-23:00 ---> Dinner and Bar "
        t=t+tim
    else:
        print("An invalid choice is entered.")
        sys.exit()
    
     
