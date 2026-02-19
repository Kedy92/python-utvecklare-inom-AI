from models import Loan, Book, Member
from database import SessionLocal
from datetime import date, timedelta

def register_loan():
    session = SessionLocal()

    book_id = int(input("Bok-ID: "))
    member_id = int(input("Medlems-ID: "))

    book = session.query(Book).filter_by(id=book_id).first()
    member = session.query(Member).filter_by(id=member_id).first()

    if not book:
        print("Boken finns ej.")
        session.close()
        return

    if book.available_copies <= 0:
        print("Inga exemplar kvar!")
        session.close()
        return

    loan = Loan(
        book_id=book_id,
        member_id=member_id,
        loan_date=date.today(),
        due_date=date.today() + timedelta(days=14)
    )

    book.available_copies -= 1

    session.add(loan)
    session.commit()
    session.close()

    print("Lån registrerat!")

def register_return():
    session = SessionLocal()
    loan_id = int(input("Lån-ID: "))

    loan = session.query(Loan).filter_by(id=loan_id).first()

    if not loan:
        print("Lån finns ej.")
        return

    if loan.return_date:
        print("Redan återlämnad.")
        return

    loan.return_date = date.today()
    loan.book.available_copies += 1

    session.commit()
    session.close()

    print("Återlämning registrerad!")

def list_active_loans():
    session = SessionLocal()
    loans = session.query(Loan).filter(Loan.return_date == None).all()

    print("\nAktiva lån:")
    for l in loans:
        print(f"[{l.id}] {l.book.title} → {l.member.first_name} {l.member.last_name}")

    session.close()

def list_overdue_loans():
    session = SessionLocal()
    today = date.today()

    loans = session.query(Loan).filter(
        Loan.return_date == None,
        Loan.due_date < today
    ).all()

    print("\nFörsenade lån:")
    for l in loans:
        print(f"[{l.id}] {l.book.title} → {l.member.first_name} {l.member.last_name} "
              f"(skulle lämnas {l.due_date})")

    session.close()