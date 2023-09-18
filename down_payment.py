price = int(input("Enter the price: "))
name_of_item = input("Enter the item you wish to purchase: ")
credit_score = int(input("Credit score: "))
if credit_score >=50:
    print("Your credit score is good enough to for a discount on this item ! ")
    Discount = 10
    Deposit = 10/100 * price
    print("************\n", "Invoice\n", "************\n")
    print("Name of item: " ,name_of_item)
    print("Discount:  ", Discount, "% of", price)
    print(Deposit)
    print("******************")
else:
    print("Your credit score is not good enough for a discount on this item!")
    print("You are not eligible for a discount !")
    print("************\n","Invoice\n","************\n")
    print("Name of item: ",name_of_item)
    Deposit = 25/100 * price
    print("Deposit: ", Deposit)
    print("******************")
