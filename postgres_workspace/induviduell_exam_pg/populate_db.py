# populate_db.py
"""
Populate the database with realistic test data.
Safe to call multiple times: it will NOT create duplicates.
"""

from datetime import date

from exam_database import get_session, create_tables
from exam_models import Brand, Product, Customer, Order, OrderItem, Review


def populate():
    """Fill the database with test data (idempotent)."""
    session = get_session()

    try:
        print("\n Lägger till testdata...")

        # ----------------------------
        # 0. Safety: avoid duplicates
        # ----------------------------
        existing_product = session.query(Product).first()
        if existing_product:
            print(" Testdata verkar redan finnas (minst en produkt finns).")
            print("   Hoppar över populate() för att undvika dubbletter.")
            return

        # ----------------------------
        # 1. Brands
        # ----------------------------
        apple = Brand(name="Apple", country="USA", founded_year=1976)
        samsung = Brand(name="Samsung", country="South Korea", founded_year=1938)
        sony = Brand(name="Sony", country="Japan", founded_year=1946)
        dell = Brand(name="Dell", country="USA", founded_year=1984)

        session.add_all([apple, samsung, sony, dell])
        session.commit()
        print("✓ Brands tillagda")

        # Refresh to ensure IDs are loaded
        for brand in (apple, samsung, sony, dell):
            session.refresh(brand)

        # ----------------------------
        # 2. Products
        # ----------------------------
        iphone = Product(
            name="iPhone 15 Pro",
            brand_id=apple.id,
            sku="APL-IP15P",
            price=12995,
            category="Smartphones",
            stock_quantity=50,
        )
        macbook = Product(
            name="MacBook Air M2",
            brand_id=apple.id,
            sku="APL-MBA",
            price=13995,
            category="Laptops",
            stock_quantity=30,
        )
        ipad = Product(
            name="iPad Air",
            brand_id=apple.id,
            sku="APL-IPAD",
            price=7495,
            category="Tablets",
            stock_quantity=40,
        )

        galaxy = Product(
            name="Galaxy S24 Ultra",
            brand_id=samsung.id,
            sku="SAM-S24U",
            price=13995,
            category="Smartphones",
            stock_quantity=45,
        )
        tab = Product(
            name="Galaxy Tab S9",
            brand_id=samsung.id,
            sku="SAM-TAB",
            price=8995,
            category="Tablets",
            stock_quantity=25,
        )

        ps5 = Product(
            name="PlayStation 5",
            brand_id=sony.id,
            sku="SNY-PS5",
            price=5495,
            category="Gaming",
            stock_quantity=15,
        )
        headphones = Product(
            name="WH-1000XM5",
            brand_id=sony.id,
            sku="SNY-WH1000",
            price=3995,
            category="Audio",
            stock_quantity=60,
        )

        xps = Product(
            name="XPS 15",
            brand_id=dell.id,
            sku="DEL-XPS15",
            price=15995,
            category="Laptops",
            stock_quantity=18,
        )
        inspiron = Product(
            name="Inspiron 14",
            brand_id=dell.id,
            sku="DEL-INS14",
            price=7995,
            category="Laptops",
            stock_quantity=35,
        )

        session.add_all(
            [iphone, macbook, ipad, galaxy, tab, ps5, headphones, xps, inspiron]
        )
        session.commit()
        print("✓ Products tillagda")

        # ----------------------------
        # 3. Customers
        # ----------------------------
        anna = Customer(
            first_name="Anna",
            last_name="Andersson",
            email="anna@email.se",
            city="Stockholm",
        )
        erik = Customer(
            first_name="Erik",
            last_name="Eriksson",
            email="erik@email.se",
            city="Göteborg",
        )
        maria = Customer(
            first_name="Maria",
            last_name="Svensson",
            email="maria@email.se",
            city="Malmö",
        )
        johan = Customer(
            first_name="Johan",
            last_name="Johansson",
            email="johan@email.se",
            city="Uppsala",
        )
        lisa = Customer(
            first_name="Lisa",
            last_name="Karlsson",
            email="lisa@email.se",
            city="Stockholm",
        )

        session.add_all([anna, erik, maria, johan, lisa])
        session.commit()
        print("✓ Customers tillagda")

        # Refresh customers for IDs
        for c in (anna, erik, maria, johan, lisa):
            session.refresh(c)

        # ----------------------------
        # 4. Orders & OrderItems
        # ----------------------------
        order1 = Order(
            customer_id=anna.id,
            order_date=date(2024, 10, 15),
            total_amount=12995,
            status="completed",
            shipping_city="Stockholm",
        )
        session.add(order1)
        session.flush()
        session.add(
            OrderItem(
                order_id=order1.id,
                product_id=iphone.id,
                quantity=1,
                unit_price=12995,
            )
        )

        order2 = Order(
            customer_id=erik.id,
            order_date=date(2024, 11, 1),
            total_amount=21490,
            status="completed",
            shipping_city="Göteborg",
        )
        session.add(order2)
        session.flush()
        session.add_all(
            [
                OrderItem(
                    order_id=order2.id,
                    product_id=macbook.id,
                    quantity=1,
                    unit_price=13995,
                ),
                OrderItem(
                    order_id=order2.id,
                    product_id=ipad.id,
                    quantity=1,
                    unit_price=7495,
                ),
            ]
        )

        order3 = Order(
            customer_id=maria.id,
            order_date=date(2024, 11, 10),
            total_amount=13995,
            status="pending",
            shipping_city="Malmö",
        )
        session.add(order3)
        session.flush()
        session.add(
            OrderItem(
                order_id=order3.id,
                product_id=galaxy.id,
                quantity=1,
                unit_price=13995,
            )
        )

        session.commit()
        print("✓ Orders + OrderItems tillagda")

        # ----------------------------
        # 5. Reviews
        # ----------------------------
        rev1 = Review(
            product_id=iphone.id,
            customer_id=anna.id,
            rating=5,
            comment="Fantastisk telefon!",
        )
        rev2 = Review(
            product_id=macbook.id,
            customer_id=erik.id,
            rating=5,
            comment="Bästa laptopen!",
        )
        rev3 = Review(
            product_id=ipad.id,
            customer_id=erik.id,
            rating=4,
            comment="Bra surfplatta",
        )
        rev4 = Review(
            product_id=ps5.id,
            customer_id=johan.id,
            rating=5,
            comment="Awesome gaming!",
        )

        session.add_all([rev1, rev2, rev3, rev4])
        session.commit()
        print("✓ Reviews tillagda")

        print("\n All testdata tillagd utan dubbletter!")

    except Exception as e:
        print(f"\n✗ Fel i populate(): {e}")
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":
    create_tables()
    populate()