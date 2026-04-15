#SMerrors
import sys
def smerr():
    f=open("SMtext.txt",'r')
    d=f.read()
    print(d)
    SMcho=int(input("Please enter a valid(1/2/3/4):"))

    if SMcho==1:
        def Rmeals():
            print("""  1.)Indian Vegeterian Meal
                       2.)Non-Vegeterian Hindu Meal
                       3.)Vegterian Jain Meal
                       4.)Kosher Meal""")    
            ch=int(input("Which meal option you would like to view?:"))
            if ch==1:
                import IVM
            elif ch==2:
                import NVHM
            elif ch==3:
                import VJM
            elif ch==4:
                import KM
        Rmeals()

    if SMcho==2:
        def MedDiet():
            f=open("MedDiet()text.txt",'r')
            d=f.read()
            print(d)
        MedDiet()
        ch=int(input("Which meal option would you like to view?(1/2/3/4/5/6):"))
        if ch==1:
            import BM
        elif ch==2:
            import DM
        elif ch==3:
            import GFM
        elif ch==4:
            import LFM
        elif ch==5:
            import LSM
        elif ch==6:
            import LLM

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
                import BabyM
            elif opt==2:
                import CM
        babymeals()

    else:
        print("""Wrong choice is entered.
        Please enter a valid choice given from the above options.""")
        sys.exit()           











