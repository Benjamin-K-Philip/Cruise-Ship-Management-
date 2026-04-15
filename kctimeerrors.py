#kctimeerrors
import sys
def kctimerr():
    print("""Below are the time slots provided for dining in 
1.)07:00-11:00 ---> Breakfast
2.)18:00-23:00 ---> Dinner""")
    time=int(input("What time would you like to dine with us?(1/2):"))
    t=""
    if time==1:
        tim="07:00-11:00 ---> Breakfast"
        t=t+tim
    elif time==2:
        tim="18:00-23:00 ---> Dinner"
        t=t+tim
    else:
        print("An invalid choice is entered.")
        sys.exit()

