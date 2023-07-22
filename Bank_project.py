import random

class BankAccount:
    def __init__(self, name, age, address, gender, balance=0):
        self.account_number = self.generate_account_number()
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender
        self.balance = balance
        self.transaction_history = []

    def generate_account_number(self):
        # Generates a random 8-digit account number
        return str(random.randint(10000000, 99999999))

    def detail(self):
        # Displays personal details of the account holder
        print("==================================================")
        print("Welcome to HBL Bank")
        print("Personal Detail:")
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Gender: {self.gender}")
        print("==================================================")

    def withdraw(self, amount1):
        if amount1 > self.balance:
            # Checks if withdrawal amount is greater than current balance
            return "Insufficient balance. Withdrawal not allowed."
        self.balance -= amount1
        self.transaction_history.append(f"Withdrawal: {amount1} Rupees")
        return f"{amount1} Rupees have been withdrawn. Remaining balance: {self.balance} Rupees."

    def deposit(self, amount2):
        self.balance += amount2
        self.transaction_history.append(f"Deposit: {amount2} Rupees")
        return f"{amount2} Rupees have been deposited. Current balance: {self.balance} Rupees."

    def show_transaction_history(self):
        # Displays the transaction history of the account
        print("==================================================")
        print(f"Transaction History for Account Number: {self.account_number}")
        for transaction in self.transaction_history:
            print(transaction)
        print("==================================================")

    def check_balance(self):
        # Checks and returns the current account balance
        return f"Account Balance: {self.balance} Rupees."


if __name__ == '__main__':
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")
    gender = input("Enter your gender: ")

    # Creates a new BankAccount instance with provided details
    a = BankAccount(name, age, address, gender)
    
    # Displays personal details of the account holder
    a.detail()

    while True:
        print("==================================================")
        print("Select an option:")
        print("1: Deposit Balance")
        print("2: Withdraw Balance")
        print("3: Show Transaction History")
        print("4: Check Balance")
        print("5: Exit")
        print("==================================================")

        user_choice = input("Enter the corresponding number: ")

        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Invalid input. Please enter a valid option.")
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            x = int(input("Enter the amount you want to deposit: "))
            print(a.deposit(x))

        elif user_choice == 2:
            y = int(input("Enter the amount you want to withdraw: "))
            print(a.withdraw(y))

        elif user_choice == 3:
            a.show_transaction_history()

        elif user_choice == 4:
            print(a.check_balance())

        elif user_choice == 5:
            print("Thank you for using HBL Bank. Goodbye!")
            break
