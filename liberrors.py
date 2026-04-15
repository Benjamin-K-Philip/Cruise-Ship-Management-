#liberrors
import sys
def liberr():
    def lib():
        f=open("libtext.txt",'r')
        d=f.read()
        print(d)
    lib()
    choices="""1 2 3 4 5 6 7 8 9 10 11 12 13
            14 15 16 17 18 19 20"""
    ch=input("Please enter a valid choice from choice 1 to choice 20:")
    if ch==1:
        import Fic
    if ch==2:
        import NonF
    if ch==3:
        import Nov
    if ch==4:
        import Mys
    if ch==5:
        import Poe
    if ch==6:
        import HisFan
    if ch==7:
        import YAF
    if ch==8:
        import His
    if ch==9:
        import SS
    if ch==10:
        import Fan
    if ch==11:
        import GN
    if ch==12:
        import AdFic
    if ch==13:
        import FT
    if ch==14:
        import CLit
    if ch==15:
        import ConLit
    if ch==16:
        import CriFic
    if ch==17:
        import Comic
    if ch==18:
        import NAF
    if ch==19:
        import Spir
    if ch==20:
        import Phil
    if ch not in choices :
        print("An invalid choice is entered.")
        sys.exit()

