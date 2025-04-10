import random

class Account():
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

class Bank():
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def generate_account_number(self):
        while True:
            acc_num = str(random.randint(11111, 2122123))
            if acc_num not in self.accounts:
                return acc_num

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            raise ValueError("Deposit can't be negative")

        acc_num = self.generate_account_number()
        account = Account(acc_num, name, initial_deposit)
        self.accounts[acc_num] = account
        self.save_to_file(account)

    def save_to_file(self, account):
        with open("accounts.txt", "a") as f:
            f.write(f"{account.account_number} | {account.name} | {account.balance}\n")

    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as file:
                for line in file:
                    data = line.strip().split("|")
                    if len(data) == 3:
                        acc_num, name, balance = data
                        self.accounts[acc_num] = Account(acc_num, name, float(balance))
        except FileNotFoundError:
            print("No existing account file found.")

    def view_account(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(f"Account Number: {account.account_number}")
            print(f"Account Holder: {account.name}")
            print(f"Balance: {account.balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= 0:
                print("Deposit amount must be positive.")
                return
            self.accounts[account_number].balance += amount
            self.update_file()
            print(f"Deposited {amount}. New balance is: {self.accounts[account_number].balance}")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= 0:
                print("Withdrawal amount must be positive.")
                return
            account = self.accounts[account_number]
            if account.balance >= amount:
                account.balance -= amount
                self.update_file()
                print(f"Withdrew {amount}. New balance is: {account.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def update_file(self):
        with open("accounts.txt", "w") as f:
            for account in self.accounts.values():
                f.write(f"{account.account_number} | {account.name} | {account.balance}\n")

# Example usage:
bank = Bank()

# Create new account
bank.create_account("John Doe", 10323)

# View account
account_number_to_search = input("Enter account number to view details: ")
bank.view_account(account_number_to_search)

# Deposit money
account_number_to_deposit = input("Enter account number to deposit to: ")
deposit_amount = float(input("Enter deposit amount: "))
bank.deposit(account_number_to_deposit, deposit_amount)

# Withdraw money
account_number_to_withdraw = input("Enter account number to withdraw from: ")
withdraw_amount = float(input("Enter withdraw amount: "))
bank.withdraw(account_number_to_withdraw, withdraw_amount)
