from models import Member
from database import SessionLocal
from datetime import date

def list_all_members():
    session = SessionLocal()
    members = session.query(Member).order_by(Member.last_name).all()
    session.close()

    print("\nMedlemmar:")
    for m in members:
        print(f"[{m.id}] {m.first_name} {m.last_name} - {m.email}")

def search_members():
    term = input("Sökterm: ")
    session = SessionLocal()

    members = session.query(Member).filter(
        Member.first_name.ilike(f"%{term}%") |
        Member.last_name.ilike(f"%{term}%") |
        Member.email.ilike(f"%{term}%")
    ).all()

    session.close()

    print("\nResultat:")
    for m in members:
        print(f"[{m.id}] {m.first_name} {m.last_name}")

def add_member():
    session = SessionLocal()

    first = input("Förnamn: ")
    last = input("Efternamn: ")
    email = input("Email: ")

    member = Member(
        first_name=first,
        last_name=last,
        email=email,
        membership_date=date.today()
    )

    session.add(member)
    session.commit()
    session.close()

    print("Medlem tillagd!")

def get_member_by_id(member_id):
    session = SessionLocal()
    member = session.query(Member).filter_by(id=member_id).first()
    session.close()
    return member