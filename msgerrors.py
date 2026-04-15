#msgerrors
import sys
def msgerr():
     print("""\n Various types of messages that are provided
1)Head Massage
2)Back & Shoulders Massage
3)Deep Tissue Massage
4)Hot stone Massages""")
     msg=int(input("Please enter a valid choice(1/2/3/4):"))
     m=""
     try:
           if msg==1:
               d="Head massage"
               m=m+d
           elif msg==2:
               d="Back and Shoulders massage"
               m=m+d
           elif msg==3:
               d="Deep tissue massage"
               m=m+d
           elif msg==4:
               d="Hot stone massage"
               m=m+d
     except:
          print("An invalid choice entered.")
          sys.exit()

