"""
GOOD CLASSES EXAMPLE
Demonstrates proper class design with error handling.
"""


# Custom exceptions - clear error signaling
class InvalidAmountError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


class AccountNotFoundError(Exception):
    pass


class BankAccount:
    """A bank account with proper error handling."""

    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self._balance = balance  # Protected - use properties

    @property
    def balance(self) -> float:
        return self._balance

    def withdraw(self, amount: float) -> float:
        """
        Withdraw money from account.

        Raises:
            InvalidAmountError: If amount is not positive
            InsufficientFundsError: If balance is too low
        """
        if amount <= 0:
            raise InvalidAmountError(f"Amount must be positive, got {amount}")

        if amount > self._balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}, balance is {self._balance}"
            )

        self._balance -= amount
        return amount

    def deposit(self, amount: float) -> float:
        """
        Deposit money to account.

        Raises:
            InvalidAmountError: If amount is not positive
        """
        if amount <= 0:
            raise InvalidAmountError(f"Amount must be positive, got {amount}")

        self._balance += amount
        return amount

    def transfer(self, other: "BankAccount", amount: float) -> None:
        """
        Transfer money to another account.

        Raises:
            InvalidAmountError: If amount is not positive
            InsufficientFundsError: If balance is too low
        """
        # Withdraw raises if there's a problem - we let it bubble up
        self.withdraw(amount)
        other.deposit(amount)


class Bank:
    """Manages a collection of accounts."""

    def __init__(self):
        self._accounts: dict[str, BankAccount] = {}

    def create_account(self, owner: str, initial_balance: float = 0) -> BankAccount:
        """Create a new account."""
        if initial_balance < 0:
            raise InvalidAmountError("Initial balance cannot be negative")

        account = BankAccount(owner, initial_balance)
        self._accounts[owner] = account
        return account

    def find_account(self, owner: str) -> BankAccount:
        """
        Find an account by owner name.

        Raises:
            AccountNotFoundError: If account doesn't exist
        """
        if owner not in self._accounts:
            raise AccountNotFoundError(f"Account for '{owner}' not found")
        return self._accounts[owner]

    def list_accounts(self) -> list[BankAccount]:
        """Return all accounts."""
        return list(self._accounts.values())


def menu():
    bank = Bank()  # Local state, not global

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
            balance_input = input("Initial balance: ")

            try:
                balance = float(balance_input)
                account = bank.create_account(owner, balance)
                print(f"Account created for {account.owner}")
            except ValueError:
                print("Balance must be a number")
            except InvalidAmountError as e:
                print(f"Error: {e}")

        elif choice == "2":
            owner = input("Account owner: ")
            amount_input = input("Amount: ")

            try:
                account = bank.find_account(owner)
                amount = float(amount_input)
                account.deposit(amount)
                print(f"Deposited {amount}. New balance: {account.balance}")
            except AccountNotFoundError as e:
                print(f"Error: {e}")
            except ValueError:
                print("Amount must be a number")
            except InvalidAmountError as e:
                print(f"Error: {e}")

        elif choice == "3":
            owner = input("Account owner: ")
            amount_input = input("Amount: ")

            try:
                account = bank.find_account(owner)
                amount = float(amount_input)
                account.withdraw(amount)
                print(f"Withdrew {amount}. New balance: {account.balance}")
            except AccountNotFoundError as e:
                print(f"Error: {e}")
            except ValueError:
                print("Amount must be a number")
            except InvalidAmountError as e:
                print(f"Error: {e}")
            except InsufficientFundsError as e:
                print(f"Error: {e}")

        elif choice == "4":
            from_owner = input("From account: ")
            to_owner = input("To account: ")
            amount_input = input("Amount: ")

            try:
                from_acc = bank.find_account(from_owner)
                to_acc = bank.find_account(to_owner)
                amount = float(amount_input)
                from_acc.transfer(to_acc, amount)
                print(f"Transferred {amount} from {from_owner} to {to_owner}")
            except AccountNotFoundError as e:
                print(f"Error: {e}")
            except ValueError:
                print("Amount must be a number")
            except InvalidAmountError as e:
                print(f"Error: {e}")
            except InsufficientFundsError as e:
                print(f"Error: {e}")

        elif choice == "5":
            owner = input("Account owner: ")

            try:
                account = bank.find_account(owner)
                print(f"Balance: {account.balance}")
            except AccountNotFoundError as e:
                print(f"Error: {e}")

        elif choice == "6":
            accounts = bank.list_accounts()
            if not accounts:
                print("No accounts")
            else:
                for acc in accounts:
                    print(f"- {acc.owner}: {acc.balance}")

        elif choice == "7":
            break


if __name__ == "__main__":
    menu()
