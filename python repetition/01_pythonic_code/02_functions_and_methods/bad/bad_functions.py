"""
BAD FUNCTIONS EXAMPLE
This code works, but demonstrates many anti-patterns.
"""

# Global variables - BAD
users = []
total_users = 0


def register_user(username, email, age):
    global total_users  # Using global keyword - FORBIDDEN

    # No type annotations
    # Function does too many things
    # Prints instead of returning
    # No proper error signaling

    if username == "" or username == None:
        print("Error: invalid username")
        return

    if "@" not in email:
        print("Error: invalid email")
        return

    if age < 18:
        print("Error: too young")
        return

    # Modifying global state - BAD
    user = {"username": username, "email": email, "age": age}
    users.append(user)
    total_users = total_users + 1

    print(f"User {username} registered!")


def list_users():
    # Prints instead of returning
    if len(users) == 0:
        print("No users")
        return

    for user in users:
        print(f"- {user['username']} ({user['email']})")


def find_user(username):
    # Returns None for "not found" - can't distinguish from errors
    for user in users:
        if user["username"] == username:
            return user
    return None  # Not found? Error? Who knows.


def menu():
    while True:
        print("\n1. Register user")
        print("2. List users")
        print("3. Find user")
        print("4. Exit")

        choice = input("Choice: ")

        if choice == "1":
            username = input("Username: ")
            email = input("Email: ")
            age = input("Age: ")
            if age.isdigit():
                register_user(username, email, int(age))
            else:
                print("Invalid age")

        elif choice == "2":
            list_users()

        elif choice == "3":
            username = input("Username to find: ")
            user = find_user(username)
            if user:
                print(f"Found: {user}")
            else:
                print("Not found")

        elif choice == "4":
            break


if __name__ == "__main__":
    menu()
