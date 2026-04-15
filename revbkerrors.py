#revvkerrors
def revbkerr():
    q=input("\nDo you want to review your booking?(Yes/No):")
    print("")

    if q in "YESYesyesYy":
        print('Name:',name,lname)
        print('Address:',adree)
        print('Cruise destination:',destination)
        print('Suite',roomtype)
        print('Total price',price)
        print('Room number:',roomno)
        time.sleep(2)
        print("""\nThank you for booking the Costa Cruise. Have a wonderful stay!
    The Concierge will guide you to you room. """)
        
    elif q in "NONonoNn":
        print("""Thank you for booking the Costa Cruise. Have a wonderful stay!
    The Concierge will guide you to you room. """)
        
    else:
        print("""Wrong choice is entered.
        Please enter a valid choice given from the above options.""")

