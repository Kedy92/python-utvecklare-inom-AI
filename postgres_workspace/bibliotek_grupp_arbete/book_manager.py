from models import Book
from database import SessionLocal

def list_all_books():
    session = SessionLocal()
    books = session.query(Book).order_by(Book.title).all()
    session.close()

    print("\nAlla böcker:")
    for b in books:
        print(f"[{b.id}] {b.title} - {b.author} ({b.category}) "
              f"{b.available_copies}/{b.total_copies}")

def search_books():
    term = input("Sökterm: ")
    session = SessionLocal()
    books = session.query(Book).filter(
        Book.title.ilike(f"%{term}%") |
        Book.author.ilike(f"%{term}%")
    ).all()
    session.close()

    print("\nSökresultat:")
    for b in books:
        print(f"[{b.id}] {b.title} - {b.author}")

def list_available_books():
    session = SessionLocal()
    books = session.query(Book).filter(Book.available_copies > 0).all()
    session.close()

    print("\nTillgängliga böcker:")
    for b in books:
        print(f"[{b.id}] {b.title} - {b.author}")

def add_book():
    session = SessionLocal()

    title = input("Titel: ")
    author = input("Författare: ")
    category = input("Kategori: ")

    book = Book(
        title=title,
        author=author,
        category=category,
        total_copies=1,
        available_copies=1
    )

    session.add(book)
    session.commit()
    session.close()
    print("Bok tillagd!")

def get_book_by_id(book_id):
    session = SessionLocal()
    book = session.query(Book).filter_by(id=book_id).first()
    session.close()
    return book