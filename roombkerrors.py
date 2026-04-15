#roombkerrors
import sys
import time 
def roombkerr():
    def roombooking():
        time.sleep(2)
        print("""\n \tRoom Reservation
    Press 1 to book seat in first floor 
    Press 2 to book seat in second floor 
    Press 3 to book seat in third floor
    Maximum capacity is 5 people \n""")
        room_a = []
        room_b = []
        room_c = []
        choice = input("Please enter a valid choice(1/2/3):")
        check = True
        while check == True:
            number = int(input("Enter for how many people is the room reserved for:"))
            if number > 5:
                print("Too many people")
            else:
                check = False
        try:       
            if choice == 1 :
                for i in range (0,number):
                    x = input("Enter visitor's name: ")
                    print("")#This is being used in order to separate multiple lines using whitespaces.
                    room_a.append(x)
            elif choice == 2:
                for i in range (0,number):
                    x = input("Enter visitor's name: ")
                    print("")
                    room_b.append(x)
            elif choice == 3:
                for i in range (0,number):
                    x = input("Enter visitor's name: ")
                    print("")
                    room_c.append(x)
        except:
            print("""Wrong choice is entered.
        Please enter a valid choice given from the above options.""")
            sys.exit()
    roombooking()

        
