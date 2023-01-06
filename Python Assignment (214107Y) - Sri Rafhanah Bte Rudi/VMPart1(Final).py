# Author: Sri Rafhanah Bte Rudi
# Admin No: 214107Y

#Part A

#Are you a vendor or not?
vendor = input("Are you a vendor (Y/N)? ").upper()

while (vendor != "Y") and (vendor != "N"):
    vendor =input("Please indicate whether vendor or not (Y/N): ").upper()
    continue #While loop to make sure pesky users input proper value

#Drink Menu
if vendor == "N":
    print("Welcome to ABC Vending Machine!")

    drinktype = {"IM": {"name": "IM", "Description": "Iced Milo", "Price" : 1.5},
                 "HM": {"name": "HM", "Description": "Hot Milo", "Price": 1.2},
                 "IC": {"name": "IC", "Description": "Iced Coffee", "Price": 1.1},
                 "HC": {"name": "HC", "Description": "Hot Coffee", "Price": 1.1},
                 "1P": {"name": "1P", "Description": "100 Plus", "Price": 1.2},
                 "CC": {"name": "CC", "Description": "Coca Cola", "Price": 1.3},
                }

    def drink_menu():
        for menu in drinktype:
            print((drinktype[menu]["name"]) + ".", (drinktype[menu]["Description"]),"(S$" + str(drinktype[menu]["Price"])
             + ")"
                 )
        print("0. Exit / Payment")
    drink_menu()

    x = 0
    p = 0
    no_of_drinks = 0
    notes = 0
    totalpayment = float(0)

    while x == 0:
            choice = input("Enter choice: ").upper()

            if choice == "IM":
               no_of_drinks = no_of_drinks + 1
               print("No of drinks selected: ",no_of_drinks)
               totalpayment = totalpayment + drinktype["IM"]["Price"]

            elif choice == "HM":
               no_of_drinks = no_of_drinks + 1
               print("No of drinks selected: ",no_of_drinks)
               totalpayment = totalpayment + drinktype["HM"]["Price"]

            elif choice == "IC":
                no_of_drinks = no_of_drinks + 1
                print("No of drinks selected: ",no_of_drinks)
                totalpayment = totalpayment + drinktype["IC"]["Price"]

            elif choice == "HC":
              no_of_drinks = no_of_drinks + 1
              print("No of drinks selected: ",no_of_drinks)
              totalpayment = totalpayment + drinktype["HC"]["Price"]

            elif choice == "1P":
               no_of_drinks = no_of_drinks + 1
               print("No of drinks selected: ", no_of_drinks)
               totalpayment = totalpayment + drinktype["1P"]["Price"]

            elif choice == "CC":
               no_of_drinks = no_of_drinks + 1
               print("No of drinks selected: ", no_of_drinks)
               totalpayment = totalpayment + drinktype["CC"]["Price"]

            elif choice == "0":
                x = 1

                payment_completed = False

                while payment_completed == False:
                    print("You need to pay $%.2f" %totalpayment)
                    print("Indicate your payment: ")
                    notes = input("Enter no. of $10 notes: ")
                    total_notes = float(notes) * 10

                    notes = input("Enter no. of $5 notes: ")
                    total_notes += float(notes) * 5

                    notes = input("Enter no. of $2 notes: ")
                    total_notes += float(notes) * 2



                    if total_notes >= totalpayment: # enough money
                        p = 1
                        print("Please pay: ", "$%.2f" % totalpayment)
                        total_price = total_notes - totalpayment
                        print("Please collect your change: $%.2f"%(total_price))
                        print("Drinks paid. Thank you")
                        payment_completed = True

                    else:
                        print("Not enough to pay for the drinks!")
                        exit1 = input("Do you want to cancel the purchase? Y/N: ").upper()

                        if exit1 == "Y":
                            print("Purchase is cancelled. Thank you")
                            payment_completed = True
                        else:
                            print("Here we go again for payment")

            else:
                print("Invalid option!")










#Vendor Menu
if vendor == "Y":
    print("Welcome to ABC Vending Machine!")

    drinktype = ["1. Add Drink Type", "2. Replenish Drink", "0. Exit"]

    drinks_list = "\n".join(drinktype)
    print(drinks_list)

    choice = input("Enter choice: ")


#Select from following choices



