#nuskatimeerrors
import sys
def nuskatimerr():
    print("""Below are the time slots provided for dining in 
1.)8:00 -11:30 --->  Breakfast
2.)11:30-13:00 --->  Brunch
3.)13:00-16:00 --->  Lunch
4.)16:00-18:00 --->  Refreshments
5.)18:00-23:00 --->  Dinner""")       
    time=int(input("Enter a valid time slot(1/2/3/4/5):"))
    t=""
    if time==1:
        tim="8:00 -11:30 ---> Breakfast"
        t=t+tim
    elif time==2:
        tim="11:30-13:00 ---> Brunch"
        t=t+tim
    elif time==3:
        tim="13:00-16:00 ---> Lunch"
        t=t+tim
    elif time==4:
        tim="16:00-18:00 ---> Refreshments"
        t=t+tim
    elif time==5:
        tim="18:00-23:00 ---> Dinner"
        t=t+tim
    else:
        print("An invalid choice is entered.")
        sys.exit()

