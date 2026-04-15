#Rmealserrors
import sys
def Rmealserr():
    print("""1.)Indian Vegeterian Meal
2.)Non-Vegeterian Hindu Meal
3.)Vegterian Jain Meal
4.)Kosher Meal""")    
    ch=int(input("Which meal option you would like to view?:"))
    try:
        if ch==1:
            import IVM
        elif ch==2:
            import NVHM
        elif ch==3:
            import VJM
        elif ch==4:
            import KM
    except:
        print("An invalid choice is entered.")
        sys.exit()

