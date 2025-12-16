import os
import datetime
import time
import random
import json

file = "Accounts.json"
accounts = {}
if not os.path.exists(file):
    with open(file, "w") as f:
        json.dump({}, f)
else:
    with open(file, "r") as f:
        accounts = json.load(f)


def save():
    with open(file, "w") as f:
        json.dump(accounts, f, indent=4)


# Generate id
"""This is a simple recursive function that generates an id for the user and checks if the id exists in the system,if not then it returns the id and if the id is present in the system it regenerates the id"""


def idGen():
    id = ""
    for _ in range(10):
        id += str(random.randint(1, 9))
    if id in accounts:
        return idGen()
    else:
        return id


# encryption
def encrypt(text):
    ntext = ""
    i = 1
    for char in text:
        ntext += chr(ord(char) + i)
        i += 1
    return ntext


# decryption
def decrypt(text):
    ntext = ""
    i = 1
    for char in text:
        ntext += chr(ord(char) - i)
        i += 1
    return ntext


# A simple login function
def login():
    id = input("Enter ID:\n")
    passw = input("Enter Password:\n")
    if id in accounts:
        if decrypt(accounts[id]["Password"]) == passw:
            return id
        else:
            print("Invalid password!")
    else:
        print("Invalid Id!")


# Create an account
def openAcc(name, id, passw):
    passw2 = input("Confirm password:\n")
    while passw != passw2:
        print("Invalid password!")
        passw2 = input("Confirm password:\n")
    accounts[id] = {
        "Name": name,
        "Balance": 0,
        "Password": encrypt(passw),
        "Transactions": [],
    }
    print("Account Details:")
    print(f"Name : {name}")
    print(f"ID : {id}")

    save()


def display():
    print("Operation succesfull!")


# deposit amounts
def deposit(id):
    try:
        amt = int(input("Enter the amount to deposit:\n"))
        while not 10000 >= amt >= 100:
            print("Maximum deposit at a time is 10000 and minimum is 100")
            try:
                amt = int(input("Enter the amount to deposit:\n"))
            except ValueError:
                print("Please Enter a number")
        accounts[id]["Balance"] += amt
        accounts[id]["Transactions"].append(
            {
                "type": "Deposit",
                "amount": amt,
                "updated_balance": accounts[id]["Balance"],
                "time": datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        save()
        display()
    except ValueError:
        print("Please enter a number ")


# withdraw amounts
def withdraw(id):
    try:
        amt = int(input("Enter the amount to withdraw:\n"))
        while amt > accounts[id]["Balance"]:
            print("Insufficient funds!")
            try:
                amt = int(input("Enter the amount to withdraw:\n"))
            except ValueError:
                print("Please Enter a Number")

        while not 10000 >= amt >= 100:
            print("Maximum withdrawal is 10000 and minimum is 100")
            try:
                amt = int(input("Enter the amount to withdraw:\n"))
            except ValueError:
                print("Please enter a number")
        accounts[id]["Balance"] -= amt
        accounts[id]["Transactions"].append(
            {
                "type": "Withdrawal",
                "amount": amt,
                "updated_balance": accounts[id]["Balance"],
                "time": datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        save()
        display()
    except ValueError:
        print("Please enter a number")


# check balance
def checkBal(id):
    print(f"Current Balance: {accounts[id]["Balance"]}")


# change password
def changePass(id, opass):
    if opass == decrypt(accounts[id]["Password"]):
        npass = input("Enter new Password:\n")
        cpass = input("Confirm new Password:\n")
        while npass != cpass:
            print("Invalid password")
            cpass = input("Confirm new Password:\n")
        accounts[id]["Password"] = encrypt(npass)
        save()
        display()
    else:
        print("Wrong password!")


# close account
def closeAccount(id, passw):
    if passw == decrypt(accounts[id]["Password"]):
        ch = input("Confirm to delete this account?(y/n)")
        if ch[0].lower() == "y":
            del accounts[id]
            save()
            display()
        else:
            return
    else:
        print("Passwords doesnt match")


# get transaction history
def transactionHistory(id):
    for transactions in accounts[id]["Transactions"]:
        for key, value in transactions.items():
            print(f"{key} : {value}", end=" | ")
        print()


def main():
    while True:
        try:
            ch = int(input("1.Login\n2.Create Account\n3.Exit:\n"))
            if ch == 1:
                x = login()
                if x:
                    while True:
                        try:
                            n = int(
                                input(
                                    "1.Deposit\n2.Withdraw\n3.Check Balance\n4.Transaction History\n5.Change Password\n6.Close Account\n7.Logout:\n"
                                )
                            )
                            if n == 1:
                                deposit(x)
                            elif n == 2:
                                withdraw(x)
                            elif n == 3:
                                checkBal(x)
                            elif n == 4:
                                transactionHistory(x)
                            elif n == 5:
                                passw = input("Enter your old password:\n")
                                changePass(x, passw)
                            elif n == 6:
                                passw = input("Enter Password to close the account:\n")
                                closeAccount(x, passw)
                            elif n == 7:
                                break
                            else:
                                print("Invalid choice!")
                        except ValueError:
                            print("Please Enter a number")
            elif ch == 2:
                name = input("Enter Your Name:\n")
                identification = idGen()
                passw = input("Enter Password for this account:\n")
                openAcc(name, identification, passw)
            elif ch == 3:
                break
            else:
                print("Invalid Choice!")
        except ValueError:
            print("Please enter a number")


main()
