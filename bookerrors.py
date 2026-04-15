#bookerrors

import sys
def bookerr():
    f=open("bookintext.txt",'r')
    d=f.read()
    print(d)
    dest=input("\nPlease enter required choice from the above options(1/2/3):")
    price=0
    if dest==1:
        destination="Egypt,Jordan and Oman"
        price=10200
    elif dest==2:
        destination="Seychelles,Kenya and Tanzania"
        price=25600       
    elif dest==3:
        destination='Madagascar'
        price=15500
    else:
        print("An invalid choice is entered.")
        sys.exit()
    

    
    
