#MDieterrors
import sys
def mdieterr():
    def MedDiet():
        f=open("MedDiet()text.txt",'r')
        d=f.read()
        print(d)
    MedDiet()
    ch=int(input("\nWhich meal option would you like to view?(1 to 6):"))
    try:
        if ch==1:
            import BM
        if ch==2:
            import DM
        if ch==3:
            import GFM
        if ch==4:
            import LFM
        if ch==5:
            import LSM
        if ch==6:
            import LLM
    except:
        print("An invalid choice is entered.")
        sys.exit()

