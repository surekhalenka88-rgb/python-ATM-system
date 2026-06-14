databsePin = 1234
balance = 10000

pin = int(input("Hey Hi! Please enter your Pin... "))

if pin == databsePin:

    while True:
        print("\n### ATM Menu ###")
        print("1. Check Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit")

        choice = int(input("Enter your Choice please..... "))

        if choice == 1:
            print("Your Account Balance is:", balance)

        elif choice == 2:
            amount = int(input("Please Enter amount that you want to Deposit... "))
            balance = balance + amount
            print("Your Deposit is Successful..")
            print("Updated Balance:", balance)

        elif choice == 3:
            amount = int(input("Please Enter Amount that you want to Withdraw: "))

            if amount > balance:
                print("Insufficient Balance......Sorry....")

            else:
                balance = balance - amount
                print("Withdraw is Successful....")
                print("Remaining Balance:", balance)

        elif choice == 4:
            print("Transaction is Completed....")
            break   # exits loop

        else:
            print("You have Selected Invalid Option. Please Check Again.")

else:
    print("You have Entered Incorrect Pin.. Please check again....")