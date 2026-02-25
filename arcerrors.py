#arcerrors
import sys
def arcerr():
    def arc():
        f=open("arctext.txt",'r')
        d=f.read()
        print(d)
    arc()
    ch=input("Please enter a valid choice(1/2):")
    if ch==1:
        import RG
    if ch==2:
        import NSG
    if ch not in "1 2":
        print("An invalid choice is entered.")
        sys.exit()
    

