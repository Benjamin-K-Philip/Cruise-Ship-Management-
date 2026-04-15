#ccerrors
import sys
def ccerr():
    f=open("cctext.txt",'r')
    d=f.read()
    print(d)                     
    print("")
    name=input("Please enter a valid name:")
    res=input("\nWould you like to book a table at our bakery?(Yes/No):")
    print("")
    if res in "YES Yes yes Y y":
        a=name
        cc.write(a)
        cc.close()
        print("""We look forward to giving you the best dining experience.
    Have a great day!""")
    elif res in "NO No no N n":
           print("Thank you for visiting Creations Cakery.")
    else:
        print("An invalid choice is entered.")
        sys.exit()
