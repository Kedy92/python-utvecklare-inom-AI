from book_manager import *
from member_manager import *
from loan_manager import *

def safe_input_number(prompt, allow_empty=False):
    """Säker input: hindrar krasher vid felaktig input."""
    while True:
        value = input(prompt).strip()

        if allow_empty and value == "":
            return None

        if value.isdigit():
            return int(value)

        print("Fel: Ange ett giltigt nummer.")

def show_menu():
    print("\n=========================")
    print(" LIBRARY SYSTEM (ORM) ")
    print("=========================")
    print("1. Book Management")
    print("2. Member Management")
    print("3. Loan Management")
    print("0. Exit")

def book_menu():
    while True:
        print("\n---- BOOK MENU ----")
        print("1. Visa alla böcker")
        print("2. Sök bok")
        print("3. Lägg till bok")
        print("4. Tillgängliga böcker")
        print("0. Back")

        c = input("Val: ").strip()

        if c == "1": 
            list_all_books()
        elif c == "2": 
            search_books()
        elif c == "3": 
            add_book()
        elif c == "4": 
            list_available_books()
        elif c == "0": 
            break
        else:
            print("Ogiltigt val. Försök igen.")

def member_menu():
    while True:
        print("\n---- MEMBER MENU ----")
        print("1. Visa medlemmar")
        print("2. Sök medlem")
        print("3. Lägg till medlem")
        print("0. Back")

        c = input("Val: ").strip()

        if c == "1": 
            list_all_members()
        elif c == "2": 
            search_members()
        elif c == "3": 
            add_member()
        elif c == "0": 
            break
        else:
            print("Ogiltigt val. Försök igen.")

def loan_menu():
    while True:
        print("\n---- LOAN MENU ----")
        print("1. Registrera lån")
        print("2. Registrera återlämning")
        print("3. Visa aktiva lån")
        print("4. Visa försenade lån")
        print("0. Back")

        c = input("Val: ").strip()

        if c == "1": 
            register_loan()
        elif c == "2": 
            register_return()
        elif c == "3": 
            list_active_loans()
        elif c == "4": 
            list_overdue_loans()
        elif c == "0": 
            break
        else:
            print("Ogiltigt val. Försök igen.")

def main():
    while True:
        show_menu()
        c = input("Val: ").strip()

        if c == "1": 
            book_menu()
        elif c == "2": 
            member_menu()
        elif c == "3": 
            loan_menu()
        elif c == "0":
            print("Avslutar...")
            break
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()