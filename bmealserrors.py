#bmealserrors
import sys
def bmealserr():
     print("1.)Baby Meals \n2.)Child Meals")
     opt=int(input("Which meal would you like to view?(1/2):"))
     try:
         if opt==1:
             import BabyM
         if opt==2:
             import CM
     except:
          print("An invalid choice entered.")
          sys.exit()
