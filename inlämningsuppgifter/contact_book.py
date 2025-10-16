#  Skapar en klass för att hantera kontaktboken
class ContactBook:
    """A class to manage a contact book with names, phone numbers, and emails."""
    
    def __init__(self):
        """Initialize an empty contact book."""
        #  Skapar en tom ordbok (dictionary) för att lagra kontakter
        self.contacts = {}
    
    def add_contact(self, name, phone, email):
        """
        Add a new contact to the contact book.
        
        Args:
            name (str): Contact's name
            phone (str): Contact's phone number
            email (str): Contact's email address
        """
        #  Kontrollerar om kontakten redan finns
        if name in self.contacts:
            print(f"\n  Contact '{name}' already exists!")
            overwrite = input("Do you want to overwrite it? (yes/no): ").lower()
            if overwrite != 'yes':
                print("Contact not added.")
                return
        
        #  Lägger till kontaktens information i dictionaryn
        self.contacts[name] = {
            'phone': phone,
            'email': email
        }
        print(f"\n✓ Contact '{name}' added successfully!")
    
    def view_all_contacts(self):
        """Display all contacts in the contact book."""
        #  Om inga kontakter finns, visa meddelande
        if not self.contacts:
            print("\n📭 No contacts found. Your contact book is empty.")
            return
        
        #  Skriver ut alla kontakter i alfabetisk ordning
        print("\n" + "="*60)
        print(" ALL CONTACTS")
        print("="*60)
        
        for name, info in sorted(self.contacts.items()):
            print(f"\nName:  {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print("-"*60)
    
    def search_contact(self, name):
        """
        Search for a contact by name.
        
        Args:
            name (str): Name of the contact to search for
        """
        #  Söker efter kontakt i dictionaryn
        if name in self.contacts:
            print("\n" + "="*60)
            print(" CONTACT FOUND")
            print("="*60)
            print(f"\nName:  {name}")
            print(f"Phone: {self.contacts[name]['phone']}")
            print(f"Email: {self.contacts[name]['email']}")
            print("-"*60)
        else:
            print(f"\n Contact '{name}' not found.")
    
    def remove_contact(self, name):
        """
        Remove a contact from the contact book.
        
        Args:
            name (str): Name of the contact to remove
        """
        #  Tar bort en kontakt om den finns
        if name in self.contacts:
            del self.contacts[name]
            print(f"\n✓ Contact '{name}' removed successfully!")
        else:
            print(f"\n Contact '{name}' not found.")


def display_menu():
    """Display the main menu options."""
    #  Visar huvudmenyn för användaren
    print("\n" + "="*60)
    print(" CONTACT BOOK MENU")
    print("="*60)
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Remove a contact")
    print("5. Exit")
    print("="*60)


def main():
    """Main function to run the contact book application."""
    #  Skapar ett nytt objekt av klassen ContactBook
    contact_book = ContactBook()
    
    print("\n" + "="*60)
    print("Welcome to Contact Book Manager!")
    print("="*60)
    
    #  Startar en loop som körs tills användaren väljer att avsluta
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            #  Lägger till en ny kontakt
            print("\n--- ADD NEW CONTACT ---")
            name = input("Enter name: ").strip()
            if not name:
                print(" Name cannot be empty!")
                continue
            phone = input("Enter phone number: ").strip()
            email = input("Enter email address: ").strip()
            contact_book.add_contact(name, phone, email)
        
        elif choice == '2':
            #  Visar alla kontakter
            contact_book.view_all_contacts()
        
        elif choice == '3':
            #  Söker efter en specifik kontakt
            name = input("\nEnter the name to search: ").strip()
            if name:
                contact_book.search_contact(name)
            else:
                print(" Name cannot be empty!")
        
        elif choice == '4':
            #  Tar bort en kontakt
            name = input("\nEnter the name to remove: ").strip()
            if name:
                contact_book.remove_contact(name)
            else:
                print(" Name cannot be empty!")
        
        elif choice == '5':
            #  Avslutar programmet
            print("\n" + "="*60)
            print("Thank you for using Contact Book Manager!")
            print("Goodbye! ")
            print("="*60 + "\n")
            break
        
        else:
            #  Felhantering om användaren skriver ett ogiltigt val
            print("\n Invalid choice! Please enter a number between 1 and 5.")


#  Startar programmet när filen körs direkt
if __name__ == "__main__":
    main()