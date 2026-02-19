"""
BAD CLASSES EXAMPLE
This code works, but demonstrates many anti-patterns.
"""

# Global state - BAD
all_accounts = []


class BankAccount:
    # No type annotations
    # No proper error signaling
    # Prints instead of returning
    # Modifies global state

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        all_accounts.append(self)  # Modifying global state - BAD

    def withdraw(self, amount):
        # Returns True/False - can't distinguish different errors
        if amount <= 0:
            print("Invalid amount")
            return False

        if amount > self.balance:
            print("Insufficient funds")
            return False

        self.balance = self.balance - amount
        print(f"Withdrew {amount}")
        return True

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return False

        self.balance = self.balance + amount
        print(f"Deposited {amount}")
        return True

    def transfer(self, other, amount):
        # Returns True/False - caller can't know WHY it failed
        if self.withdraw(amount):
            other.deposit(amount)
            return True
        return False


def find_account(owner):
    # Returns None - can't distinguish "not found" from other errors
    for account in all_accounts:
        if account.owner == owner:
            return account
    return None


def menu():
    while True:
        print("\n1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Check balance")
        print("6. List accounts")
        print("7. Exit")

        choice = input("Choice: ")

        if choice == "1":
            owner = input("Owner name: ")
            balance = input("Initial balance: ")
            if balance.isdigit():
                BankAccount(owner, int(balance))
                print(f"Account created for {owner}")
            else:
                print("Invalid balance")

        elif choice == "2":
            owner = input("Account owner: ")
            account = find_account(owner)
            if account:
                amount = input("Amount: ")
                if amount.isdigit():
                    account.deposit(int(amount))
                else:
                    print("Invalid amount")
            else:
                print("Account not found")

        elif choice == "3":
            owner = input("Account owner: ")
            account = find_account(owner)
            if account:
                amount = input("Amount: ")
                if amount.isdigit():
                    account.withdraw(int(amount))
                else:
                    print("Invalid amount")
            else:
                print("Account not found")

        elif choice == "4":
            from_owner = input("From account: ")
            to_owner = input("To account: ")
            from_acc = find_account(from_owner)
            to_acc = find_account(to_owner)

            if from_acc and to_acc:
                amount = input("Amount: ")
                if amount.isdigit():
                    if from_acc.transfer(to_acc, int(amount)):
                        print("Transfer complete")
                    else:
                        print("Transfer failed")
                else:
                    print("Invalid amount")
            else:
                print("Account not found")

        elif choice == "5":
            owner = input("Account owner: ")
            account = find_account(owner)
            if account:
                print(f"Balance: {account.balance}")
            else:
                print("Account not found")

        elif choice == "6":
            if not all_accounts:
                print("No accounts")
            else:
                for acc in all_accounts:
                    print(f"- {acc.owner}: {acc.balance}")

        elif choice == "7":
            break


if __name__ == "__main__":
    menu()
