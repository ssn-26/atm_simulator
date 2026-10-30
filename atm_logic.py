
import sys
from getpass import getpass
from datetime import datetime
import json


pin = "1234"
balance = 5000
history = {}
again = True
b_status = False


def verif_pin(x):

    return x == "1234"


def show_bal():

    print("Your balance is : ₹", balance)

    
def time_stamp():

    stamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(stamp)


if __name__ == "__main__":

    e_pin = getpass("Enter the PIN: ")

    for i in range(2, -1, -1):

        if verif_pin(e_pin):

            print("PIN verified")
            break

        else:

            remaining = i

            if remaining > 0:

                print(f"Incorrect pin\nYou have {remaining} attempts remaining\nTry again")
                e_pin = getpass("Enter the PIN: ")

            else:

                print("Incorrect pin. No attempts left. Account blocked.")
                b_status = True

                sys.exit()
                
    while again:

        menu_input = input("__________ ATM MENU __________\n1) display balance    2) withdraw\n3) deposit            4) history\n5) check transaction  6) Change password\n7) exit\n").strip()

        if menu_input.isdigit():

            choice = int(menu_input)

        else:

            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if choice == 1:

            show_bal()
            time_stamp()

            now_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            history["bal_check"] = f"checked balance at {now_str} which was {balance}"
            
            user_input = input("Would you like to go to the menu again? :").strip().lower()
            again = user_input in ["true", "yes", "y", "1"]

        elif choice == 2:
           
            w_amt = float(input("Enter withdraw amt: "))

            if w_amt > 0:
                
                if w_amt <= balance:
                    
                    balance = balance - w_amt
                    print("Withdrawal successful")
                    
                    show_bal()
                    time_stamp()
                    
                    now_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    history["withdraw"] = f"withdrawn amt {w_amt} at {now_str}"
                    
                    user_input = input("Would you like to go to the menu again? : ").strip().lower()
                    again = user_input in ["true", "yes", "y", "1"]
                
                else:

                    print("Withdraw amount is more than balance")
                    continue

            else:

                print("Invalid amount")
                break

        elif choice == 3:

            d_amt = float(input("Enter the amt to be deposited: "))

            if d_amt > 0:

                balance = balance + d_amt  # Fixed deposit logic

                show_bal()
                time_stamp()
                
                now_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                history["deposit"] = f"deposited amt {d_amt} at {now_str}"
                
                user_input = input("Would you like to go to the menu again? : ").strip().lower()
                again = user_input in ["true", "yes", "y", "1"]

            else:

                print("Invalid amount")
                break

        elif choice == 4:

            record = json.dumps(history, indent=4)
            print(record)

            user_input = input("Would you like to go to the menu again? : ").strip().lower()
            again = user_input in ["true", "yes", "y", "1"]

        elif choice == 5:

            t = input("Enter the transaction you need to check (bal_check, withdraw, deposit): ").strip()

            for j in history:

                if j == t :

                    print("found : ",history[j])
                    break

            else:

                print("Transaction not found in history.")

        elif choice == 6:

            pass

        elif choice == 7:

            print("Thanks for using our banking service \nVisit again")
            again = False

            break
        
        else:

            print("Incorrect input try again")
            continue