import os
import json
import random


def loading_data(x: str):
    with open(x, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def saving(file, dictionary):
    with open(file, "w") as f:
        json.dump(dictionary, f, indent=4)


system = {}
data = "data.json"
if not os.path.exists(data):
    with open(data, "w") as f:
        f.write("")
else:
    system = loading_data(data)


def account_no_generator():
    x = "123456789012345"
    acc = ""
    for i in range(10):
        acc += random.choice(x)
    if acc in system:
        return account_no_generator()
    else:
        return acc


def open_account(name, acc_no, pin):
    system[acc_no] = {"name": name, "balance": 0, "pin": pin}
    saving(data, system)


def show_balance(acc_no, pin):
    if acc_no in system:
        if pin == system[acc_no]["pin"]:
            return (
                f"{system[acc_no]["name"]} your balance is ₹{system[acc_no]["balance"]}"
            )
        else:
            return "incorrect pin"
    else:
        return "Invalid Account Id"


def deposit(acc_no, pin, amount: int):
    if acc_no in system:
        if pin == system[acc_no]["pin"]:
            system[acc_no]["balance"] += amount
            print("deposit succesfull")
            saving(data, system)
        else:
            print("Incorrect pin")
    else:
        print("Invalid Account Id")


def withdraw(acc_no, pin, amount):
    if acc_no in system:
        if pin == system[acc_no]["pin"]:
            if amount <= system[acc_no]["balance"]:
                if amount >= 500:
                    print("Withdrawal succesfull")
                    system[acc_no]["balance"] -= amount
                    saving(data, system)
                else:
                    print("Withdrawal amount should not be less than 500 Rupees")
            else:
                print("Insufficient Funds")
        else:
            print("Incorrect pin")
    else:
        print("Account Id not found")


def change_pin(acc_no, pin):
    if acc_no in system:
        if pin == system[acc_no]["pin"]:
            new_pin = input("Enter new pin")
            if new_pin.isdigit() and 3 < len(new_pin) < 5:
                system[acc_no]["pin"] = new_pin
                print("Pin changed succesfully")
                saving(data, system)
            else:
                print("Pin should contain only digits and should be 4 digits ")
        else:
            print("Incorrect pin")
    else:
        print("Account Id Not found")


def delete_account(acc_no, pin):
    if acc_no in system:
        if pin == system[acc_no]["pin"]:
            del system[acc_no]
            print("Account deleted succesfully")
            saving(data, system)
        else:
            print("Invalid pin")
    else:
        print("Account Id not found")


def main():
    while True:
        print("\n\nWelcome To Orbit Bank")
        print("Enter 1 to open an account")
        print("Enter 2 to show balance")
        print("Enter 3 to deposit money in your account")
        print("Enter 4 to withdraw money from your account")
        print("Enter 5 to change pin")
        print("Enter 6 to delete your account")
        print("Enter 7 to exit")
        try:
            x = int(input("Enter your choice"))
        except ValueError:
            print("Enter an integer")
            continue
        if x == 1:
            name = input("Enter Your Full name")

            acc_no = account_no_generator()
            print(f"your account number is {acc_no}")
            pin = input("Enter your pin")
            if pin.isdigit() and len(pin) == 4:
                open_account(name, acc_no, pin)
                print("Account succesfully created")
            else:
                print("Pin should contain numbers only and must be 4 digit")

        elif x == 2:
            acc_no = input("Enter your account number")
            pin = input("Enter your pin")
            print(show_balance(acc_no, pin))
        elif x == 3:
            acc_no = input("Enter your account number")
            pin = input("Enter your pin")
            try:
                amount = int(input("Enter the amount which you want to deposit"))
                if amount >= 500:
                    deposit(acc_no, pin, amount)
                else:
                    print("Deposit could not be less than 500 Rupees")
            except ValueError:
                print("Enter an integer")

        elif x == 4:
            acc_no = input("Enter your account number")
            pin = input("Enter your pin")
            try:
                amount = int(input("Enter the amount which you want to withdraw"))
                withdraw(acc_no, pin, amount)
            except ValueError:
                print("Amount should be an integer")

        elif x == 5:
            acc_no = input("Enter your account number")
            pin = input("Enter your old  pin")
            change_pin(acc_no, pin)
        elif x == 6:
            acc_no = input("Enter your account number")
            pin = input("Enter your  pin")
            delete_account(acc_no, pin)
        elif x == 7:
            print("Thank you for banking with us")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
