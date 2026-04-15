#f24errors
import sys
def f24err():
    f=open("f24text.txt",'r')
    d=f.read()
    print(d)
    print("")
    name=input("Please enter a valid name:")
    res=input("\nWould you like to book a table at our restaurant?(Yes/No):")
    print("")
    if res in "YES Yes yes Y y":
        a=name
        f24.write(a)
        f24.close()
        print("""We look forward to giving you the best dining experience.
                 Have a great day!""")
    elif res in "NO No no N n":
        print("Thank you for visiting Floor 24.")
    else:
        print("An invalid choice is entered.")
        sys.exit()
    
