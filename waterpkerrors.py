#waterpkerrors
import sys
def waterpkerr():
    print("""Settle aboard a gleaming yacht with sunbathing and seating decks,
and absorb the landmarks as you glide over""")
    print("")
    q=input("Would you like to book a ticket for waterpark?(Yes/No):")
    if q in"Yes YES yes Y y":
        n=int(input("How many tickets would you like to book?:"))
        waterpark=[]
        for i in range(n):   
            name=input("Enter name of visitor:")
            waterpark.append(name)
        print("""Please feel free to visit the waterpark
    from 10am-8pm.
    Thank you for visiting the waterpark .""")
    elif q in "NO No no N n":
        print("""Thank you for visiting the waterpark.
        Have a good day.""")
    else:
        print("\nAn invalid choice is entered.")
        sys.exit()
