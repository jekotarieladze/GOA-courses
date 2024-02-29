class BankAccount:
    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Saddly you do not have enough money to make this transaction. Withdrawal canceled.")
        else:
            print("Invalid withdrawal amount.")

def main():
    print("Welcome to the Banking System!")

    # make an account
    owner_name = input("Enter your name: ")
    initial_balance = float(input("Enter the initial balance: "))
    account = BankAccount(owner_name, initial_balance)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter the deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter the withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Current balance for {account.owner_name}: ${account.balance}")
        elif choice == "4":
            print("Exiting the Banking System. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()