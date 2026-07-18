#Washing machine Menu (same as atm logic)
current_mode = None
wash_time = 0
while True:
    print("\n--- washing machine menu ---")
    print("1. select mode")
    print("2. start wash")
    print("3. check time remaining")
    print("4. exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Mode:1.Quick 2.Normal 3.Heavy")
        mode_choice = int(input("Select mode: "))
        
        if mode_choice ==1:
            current_mode = "Quick"
            wash_time = 15
        elif mode_choice == 2:
            current_mode = "Normal"
            wash_time = 30
        elif mode_choice ==3:
            current_mode = "Heavy"
            wash_time = 45
        else:
            print("INVALID MODE")
            continue

        print(current_mode,"mode selected.time: ",wash_time,"min")
    elif choice == 2:
        if current_mode is None:
            print("SELECT A MODE FIRST")
        else:
            print("wash started in",current_mode,"mode for",wash_time,"min")
    elif choice ==3:
        if current_mode is None:
            print("NO MODE IS SELECTED YET")
        else:
            print("time reamaining: ",wash_time,"min")
    elif choice ==4:
        print("<-- THANK YOU --> ")
        break
    else:
        print("INVALID CHOICE.")                                        

