#msgtimerros
import sys
def msgtimerr():
     print("""\n Time slots that are provided
1)Morning:- 8:00-10:00
2)Afternoon:- 1:00-3:00
3)Evening:- 5:00-6:00""")
     timing=int(input("Please enter a valid choice(1/2/3):"))
     t=""
     try:
          if timing==1:
               tim="Morning 8:00-10:00"
               t=t+tim
          elif timing==2:
                tim=" Afternoon 1:00-3:00"
                t=t+tim
          elif timing==3:
                tim="Evening 5:00-6:00"
                t=t+tim
     except:
         print("An invalid choice is entered.")
         sys.exit()


