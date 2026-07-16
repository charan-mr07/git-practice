#ATM logic - basic concept (while loop)

balance = 1000       # starting balance 
correct_pin = 1234

pin = int(input("Enter your PIN: "))
if pin != correct_pin:
    print("Incorrect PIN. Access denied.")
else:
    while True:
        print("\n---- ATM Menu ----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("Your balance is:",balance)
        elif choice == 2:
            amount = int(input("Enter Deposit amount: "))
            balance = balance + amount
            print("Deposited successfully. New balance:",balance)
        elif choice == 3:
            amount = int(input("Enter withdraw amount: "))
            if amount > balance:
                print("Insuffiicent balance")
            else:
                balance = balance - amount 
                print("Withdraw successfully. New balance:",balance)
        elif choice == 4:
            print("Thank you for using ATM. Goodbye!")
            break 
        else:
            print("Invalid choice, try again.")
# while True - infinite loop
# break - loop to exit
# if-elif-else                                

