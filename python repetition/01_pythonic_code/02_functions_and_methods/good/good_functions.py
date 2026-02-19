"""
GOOD FUNCTIONS EXAMPLE
Demonstrates proper function design with error handling.
"""


# Custom exceptions - clear error signaling
class InvalidUsernameError(Exception):
    pass

class InvalidEmailError(Exception):
    pass

class UserTooYoungError(Exception):
    pass

class UserNotFoundError(Exception):
    pass


# Type definitions
from typing import TypedDict

class User(TypedDict):
    username: str
    email: str
    age: int


# Single-responsibility functions
def validate_username(username: str) -> str:
    if not username or not username.strip():
        raise InvalidUsernameError("Username cannot be empty")
    return username.strip()


def validate_email(email: str) -> str:
    if "@" not in email:
        raise InvalidEmailError(f"Invalid email: {email}")
    return email.strip()


def validate_age(age: int) -> int:
    if age < 18:
        raise UserTooYoungError(f"Must be 18+, got {age}")
    return age


def create_user(username: str, email: str, age: int) -> User:
    """Create a user. Raises specific exceptions for each validation error."""
    validated_username = validate_username(username)
    validated_email = validate_email(email)
    validated_age = validate_age(age)

    return {
        "username": validated_username,
        "email": validated_email,
        "age": validated_age
    }


def find_user(users: list[User], username: str) -> User:
    """Find a user by username. Raises UserNotFoundError if not found."""
    for user in users:
        if user["username"] == username:
            return user
    raise UserNotFoundError(f"User '{username}' not found")


def menu():
    users: list[User] = []  # Local state, not global

    while True:
        print("\n1. Register user")
        print("2. List users")
        print("3. Find user")
        print("4. Exit")

        choice = input("Choice: ")

        if choice == "1":
            username = input("Username: ")
            email = input("Email: ")
            age_input = input("Age: ")

            try:
                age = int(age_input)
                user = create_user(username, email, age)
                users.append(user)
                print(f"User {user['username']} registered!")
            except ValueError:
                print("Age must be a number")
            except InvalidUsernameError as e:
                print(f"Username error: {e}")
            except InvalidEmailError as e:
                print(f"Email error: {e}")
            except UserTooYoungError as e:
                print(f"Age error: {e}")

        elif choice == "2":
            if not users:
                print("No users")
            else:
                for user in users:
                    print(f"- {user['username']} ({user['email']})")

        elif choice == "3":
            username = input("Username to find: ")
            try:
                user = find_user(users, username)
                print(f"Found: {user}")
            except UserNotFoundError as e:
                print(f"Error: {e}")

        elif choice == "4":
            break


if __name__ == "__main__":
    menu()
