# Author: Sri Rafhanah Bte Rudi
# Admin No: 214107Y

#Part 2

#Are you a vendor or not?

drinktypedict1 = {"IM": {"Drink_id": "IM", "Description": "Iced Milo", "Price": 1.5, "Quantity": 2},
                  "HM": {"Drink_id": "HM", "Description": "Hot Milo", "Price": 1.2, "Quantity": 20},
                  "IC": {"Drink_id": "IC", "Description": "Iced Coffee", "Price": 1.1, "Quantity": 2},
                  "HC": {"Drink_id": "HC", "Description": "Hot Coffee", "Price": 1.1, "Quantity": 0},
                  "1P": {"Drink_id": "1P", "Description": "100 Plus", "Price": 1.2, "Quantity": 50},
                  "CC": {"Drink_id": "CC", "Description": "Coca Cola", "Price": 1.3, "Quantity": 50},
                  }
drinktypedict2 = {"IM": {"Drink_id": "IM", "Description": "Iced Milo", "Price": 1.5, "Quantity": 0},
                  "HM": {"Drink_id": "HM", "Description": "Hot Milo", "Price": 1.2, "Quantity": 0},
                  "IC": {"Drink_id": "IC", "Description": "Iced Coffee", "Price": 1.1, "Quantity": 0},
                  "HC": {"Drink_id": "HC", "Description": "Hot Coffee", "Price": 1.1, "Quantity": 0},
                  "1P": {"Drink_id": "1P", "Description": "100 Plus", "Price": 1.2, "Quantity": 0},
                  "CC": {"Drink_id": "CC", "Description": "Coca Cola", "Price": 1.3, "Quantity": 0},
                  }
vendor = input("Are you a vendor (Y/N)? ").upper()

while (vendor != "Y") and (vendor != "N"):
    vendor =input("Please indicate whether vendor or not (Y/N): ").upper()
    continue #While loop to make sure pesky users input proper value

#Drink Menu
if vendor == "N":
    print("Welcome to ABC Vending Machine!")
    print("Select from the following choices to continue:  ")


    def drink_menu(): # This prints the dictionary out
        for menu in drinktypedict1:
            print((drinktypedict1[menu]["Drink_id"]) + ".", (drinktypedict1[menu]["Description"]),"(S$" + str(drinktypedict1[menu]["Price"])
             + ")", "Qty:" + str((drinktypedict1[menu]["Quantity"]))
                 )
        print("0. Exit / Payment")
    drink_menu() # Call the function drink menu

    x = 0
    p = 0
    no_of_drinks = 0
    notes = 0
    totalpayment = float(0)

    while x == 0:
            choice = input("Enter choice: ").upper() #Pick the drink ID
            drinktypedict2 = {"IM": {"Drink_id": "IM", "Description": "Iced Milo", "Price": 1.5, "Quantity": 0},
                              "HM": {"Drink_id": "HM", "Description": "Hot Milo", "Price": 1.2, "Quantity": 0},
                              "IC": {"Drink_id": "IC", "Description": "Iced Coffee", "Price": 1.1, "Quantity": 0},
                              "HC": {"Drink_id": "HC", "Description": "Hot Coffee", "Price": 1.1, "Quantity": 0},
                              "1P": {"Drink_id": "1P", "Description": "100 Plus", "Price": 1.2, "Quantity": 0},
                              "CC": {"Drink_id": "CC", "Description": "Coca Cola", "Price": 1.3, "Quantity": 0},
                              }

            if choice == "IM": # If drink ID is IM
                if (drinktypedict1[choice]["Quantity"]) != (drinktypedict2[choice]["Quantity"]): #IM in dict1 quantity != dict2
                    drinktypedict2["IM"]["Quantity"] = (drinktypedict2["IM"]["Quantity"]) + 1 #Adds to the 2nd dictionary (Follows up in the for loop)
                    no_of_drinks = no_of_drinks + 1
                    totalpayment = totalpayment + drinktypedict1["IM"]["Price"]
                    print("No of drinks selected: ", no_of_drinks)

                    for key in drinktypedict1:
                        drinktypedict1[key]["Quantity"] = drinktypedict1[key]["Quantity"] - drinktypedict2[key]["Quantity"]  # Updates main
                    print("Updated Stocks:") # Prints the stock
                    for key in drinktypedict1:
                        print(key, ' : ', drinktypedict1[key])
                else:
                    print(drinktypedict1["IM"]["Description"], "is out of stock!!") #Prints the drink is out of stock
                    print("Updated Stocks:")
                    for key in drinktypedict1:
                        print(key, ' : ', drinktypedict1[key])

            elif choice == "HM":
                if (drinktypedict1[choice]["Quantity"]) != (drinktypedict2[choice]["Quantity"]): #HM in dict1 quantity != dict2
                    drinktypedict2["HM"]["Quantity"] = (drinktypedict2["HM"]["Quantity"]) + 1 #Adds to the 2nd dictionary (Follows up in the for loop)
                    no_of_drinks = no_of_drinks + 1
                    totalpayment = totalpayment + drinktypedict1["HM"]["Price"]
                    print("No of drinks selected: ", no_of_drinks)

                    for key in drinktypedict1:
                        drinktypedict1[key]["Quantity"] = drinktypedict1[key]["Quantity"] - drinktypedict2[key]["Quantity"]  # Updates main dict
                    print("Updated Stocks:")
                    for key in drinktypedict1:
                        print(key, ' : ', drinktypedict1[key])
                else:
                    print(drinktypedict1["HM"]["Description"], "is out of stock!!") #Prints the drink is out of stock
                    print("Updated Stocks:")
                    for key in drinktypedict1:
                        print(key, ' : ', drinktypedict1[key])

            elif choice == "IC":
                if (drinktypedict1[choice]["Quantity"]) != (drinktypedict2[choice]["Quantity"]): #IC in dict1 quantity != dict2
                    drinktypedict2["IC"]["Quantity"] = (drinktypedict2["IC"]["Quantity"]) + 1 #Adds to the 2nd dictionary (Follows up in the for loop)
                    no_of_drinks = no_of_drinks + 1
                    totalpayment = totalpayment + drinktypedict1["IC"]["Price"]
                    print("No of drinks selected: ", no_of_drinks)

                    for key in drinktypedict1:
                        drinktypedict1[key]["Quantity"] = drinktypedict1[key]["Quantity"] - drinktypedict2[key]["Quantity"]  # Updates main dict
                    print("Updated Stocks:")
                    for key in drinktypedict1:
                        print(key, ' : ', drinktypedict1[key])
                else:
                    print(drinktypedict1["IC"]["Description"], "is out of stock!!") #Prints the drink is out of stock
                    print("Updated Stocks:")
                    for key in drinktypedict1:
                        print(key, ' : ', drinktypedict1[key])
            elif choice == "HC":
                if (drinktypedict1[choice]["Quantity"]) != (drinktypedict2[choice]["Quantity"]): #HC in dict1 quantity != dict2
                    drinktypedict2["HC"]["Quantity"] = (drinktypedict2["HC"]["Quantity"]) + 1 #Adds to the 2nd dictionary (Follows up in the for loop)
                    no_of_drinks = no_of_drinks + 1
                    totalpayment = totalpayment + drinktypedict1["HC"]["Price"]
                    print("No of drinks selected: ", no_of_drinks)

                    for key in drinktypedict1:
                        drinktypedict1[key]["Quantity"] = drinktypedict1[key]["Quantity"] - drinktypedict2[key]["Quantity"]  # Updates main dict
                    print("Updated Stocks:")
                    for key in drinktypedict1:
                        print(key, ' : ', drinktypedict1[key])
                else:
                    print(drinktypedict1["HC"]["Description"], "is out of stock!!") #Prints the drink is out of stock
                    print("Updated Stocks:")
                    for key in drinktypedict1:
                        print(key, ' : ', drinktypedict1[key])
            elif choice == "1P":
                if (drinktypedict1[choice]["Quantity"]) != (drinktypedict2[choice]["Quantity"]): #1P in dict1 quantity != dict2
                    drinktypedict2["1P"]["Quantity"] = (drinktypedict2["1P"]["Quantity"]) + 1 #Adds to the 2nd dictionary (Follows up in the for loop)
                    no_of_drinks = no_of_drinks + 1
                    totalpayment = totalpayment + drinktypedict1["1P"]["Price"]
                    print("No of drinks selected: ", no_of_drinks)

                    for key in drinktypedict1:
                        drinktypedict1[key]["Quantity"] = drinktypedict1[key]["Quantity"] - drinktypedict2[key]["Quantity"]  # Updates main dict
                    print("Updated Stocks:")
                    for key in drinktypedict1:
                        print(key, ' : ', drinktypedict1[key])
                else:
                    print(drinktypedict1["1P"]["Description"], "is out of stock!!") #Prints the drink is out of stock
                    print("Updated Stocks:")
                    for key in drinktypedict1:
                        print(key, ' : ', drinktypedict1[key])

            elif choice == "CC":
                if (drinktypedict1[choice]["Quantity"]) != (drinktypedict2[choice]["Quantity"]): #CC in dict1 quantity != dict2
                    drinktypedict2["CC"]["Quantity"] = (drinktypedict2["CC"]["Quantity"]) + 1 #Adds to the 2nd dictionary (Follows up in the for loop)
                    no_of_drinks = no_of_drinks + 1
                    totalpayment = totalpayment + drinktypedict1["CC"]["Price"]
                    print("No of drinks selected: ", no_of_drinks)

                    for key in drinktypedict1:
                        drinktypedict1[key]["Quantity"] = drinktypedict1[key]["Quantity"] - drinktypedict2[key]["Quantity"]  # Updates main dict
                    print("Updated Stocks:")
                    for key in drinktypedict1:
                        print(key, ' : ', drinktypedict1[key])
                else:
                    print(drinktypedict1["CC"]["Description"], "is out of stock!!") #Prints the drink is out of stock
                    print("Updated Stocks:")
                    for key in drinktypedict1:
                        print(key, ' : ', drinktypedict1[key])


            elif choice == "0": #Payment or exit
                x = 1
                payment_completed = False

                while payment_completed == False: # Notes for payment
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

    vendorchoose = ["1. Add Drink Type", "2. Replenish Drink", "0. Exit"]

    drinks_list = "\n".join(vendorchoose) # Split objects in drinktype into 3 lines
    print(drinks_list)

    choice = int(input("Enter choice: "))  # Select from following choices

    if choice == 1:  #While choice's input exists in vendorchoose's list, this runs
        x = 0

        while x == 0: #Looper
            drinkchoice = input("Enter Drink ID: ").upper()
            if (drinkchoice in drinktypedict1) is True:
                print("Drink_id Exists!")

            else:  #If it is a new drink, then add description/price/quantity
                x = 1

        newDrink1 = input("Enter Description of Drink: ")
        newDrink2 = float(input("Enter Price of Drink: $"))
        newDrink3 = int(input("Enter Quantity of Drink: "))


        def add_drink_type(Drink_id, Description, Price, Quantity):
            drinktypedict1[drinkchoice] = {Drink_id: drinkchoice, Description: newDrink1, Price: newDrink2, Quantity: newDrink3}  # This will update new drink in main dictionary(Dict1)
            drinktypedict2[drinkchoice] = {Drink_id: drinkchoice, Description: newDrink1, Price: newDrink2, Quantity: 0}  # Updates new drink in 2nd dictionary

            for key2 in drinktypedict1:
                print(key2, " : ", drinktypedict1[key2])
        add_drink_type("Drink_id", "Description", "Price", "Quantity")


    if choice == 2:
        for key3 in drinktypedict1:
            print(key3, " : ", drinktypedict1[key3])
            counter1 = True
        def replenish_drink():
            while counter1 == True:
                enter_id = input("Enter Drink ID: ").upper()

                if enter_id == "0":
                    print("Please restart")
                    for key3 in drinktypedict1:
                        print(key3, " : ", drinktypedict1[key3])
                    continue

                if enter_id in drinktypedict1:
                    if drinktypedict1[enter_id]["Quantity"] > 5:
                        print("No need to replenish. Quantity is greater than 5.")

                    elif drinktypedict1[enter_id]["Quantity"] <= 5:
                        topup = int(input("Enter Quantity: "))
                        replenish = topup + drinktypedict1[enter_id]["Quantity"]
                        drinktypedict1[enter_id]["Quantity"] = replenish
                        print(drinktypedict1[enter_id]["Description"], "has been topped up!")
                        continue #Return the loop, add more drinks
                else:
                    print("No drink with this drink id. Try again.")
                    continue
        replenish_drink()


    if choice == 0:
        print("Exiting choice. Please run again.")
