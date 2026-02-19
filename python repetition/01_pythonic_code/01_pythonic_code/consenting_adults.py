"""
"We are all consenting adults" - Python's Philosophy of Trust

Python doesn't enforce rules - it trusts developers to follow conventions.
This means the skill ceiling is high: you MUST understand the culture.

In languages like Java or C#, the compiler stops you from breaking rules.
In Python, nothing stops you. You are trusted to know better.
"""


# =============================================================================
# CONSTANTS - Python has no real constants
# =============================================================================

# Convention: UPPERCASE = "don't change this"
# Reality: Python lets you change it anyway

MAX_LOGIN_ATTEMPTS = 3
DATABASE_URL = "postgresql://localhost:5432/myapp"
API_TIMEOUT_SECONDS = 30

# Nothing stops you from doing this:
MAX_LOGIN_ATTEMPTS = 999  # Bad practice, but Python allows it

# Why? Because Python trusts you. If you override a constant,
# you probably have a good reason (testing, special case, etc.)
# The responsibility is on YOU to know what you're doing.


# =============================================================================
# PROTECTED AND PRIVATE - Convention, not enforcement
# =============================================================================

class BankAccount:
    """
    A class demonstrating Python's naming conventions for visibility.

    _single_underscore = "protected" - internal use, but accessible
    __double_underscore = "private" - name mangled, but still accessible
    """

    def __init__(self, owner: str, initial_balance: float):
        self.owner = owner                    # Public - use freely
        self._balance = initial_balance       # Protected - internal use
        self.__pin = "1234"                   # Private - name mangled

    def deposit(self, amount: float) -> None:
        """Public method - the intended interface."""
        if amount > 0:
            self._balance += amount
            self._log_transaction("deposit", amount)

    def _log_transaction(self, transaction_type: str, amount: float) -> None:
        """
        Protected method - intended for internal use only.
        The underscore says: "Don't call this from outside the class."
        But Python won't stop you if you do.
        """
        print(f"[LOG] {transaction_type}: {amount}")

    def __validate_pin(self, pin: str) -> bool:
        """
        Private method - name mangled to _BankAccount__validate_pin.
        Harder to access, but still possible.
        We barely use this pattern, its more common with _underscore
        """
        return pin == self.__pin


# Demonstration of what Python ALLOWS (but you shouldn't do):

account = BankAccount("Alice", 1000.0)

# Accessing protected attribute - works fine
print(account._balance)  # 1000.0 - Python trusts you

# Calling protected method - works fine
account._log_transaction("test", 50)  # Python trusts you

# Accessing "private" attribute - requires knowing the mangled name
print(account._BankAccount__pin)  # "1234" - Python STILL trusts you

# The point: Python gives you the tools, not the restrictions.
# A skilled Python developer knows NOT to do these things,
# even though Python allows them.


# =============================================================================
# WHY THIS MATTERS - Real world example
# =============================================================================

class DatabaseConnection:
    """
    In production code, you'll see patterns like this.
    The underscores communicate intent to other developers.
    """

    _instance = None  # Protected class variable - singleton pattern

    def __init__(self, connection_string: str):
        self._connection_string = connection_string
        self._is_connected = False
        self.__connection = None  # The actual connection object

    def connect(self) -> None:
        """Public interface - use this."""
        if not self._is_connected:
            self._establish_connection()
            self._is_connected = True

    def _establish_connection(self) -> None:
        """
        Protected - implementation detail.

        Subclasses might override this for different database types,
        but external code should never call this directly.
        """
        print(f"Connecting to {self._connection_string}...")
        # self.__connection = actual_db_connect(...)

    def execute(self, query: str):
        """Public interface for running queries."""
        if not self._is_connected:
            raise RuntimeError("Not connected to database")
        return self._execute_query(query)

    def _execute_query(self, query: str):
        """Protected - the actual query execution."""
        print(f"Executing: {query}")
        # return self.__connection.execute(query)


# =============================================================================
# THE TAKEAWAY
# =============================================================================

"""
Python's philosophy:

1. UPPERCASE_CONSTANTS - "This shouldn't change, but I trust you"
2. _protected - "This is internal, but I trust you"
3. __private - "This is really internal, but I STILL trust you"

Other languages: "You CAN'T do this"
Python: "You SHOULDN'T do this, but you're an adult"

This is why understanding Python culture matters so much.
The language won't save you from bad decisions.
"""
