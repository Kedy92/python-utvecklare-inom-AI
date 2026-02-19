# exam_main.py
"""
Simple CLI main program for the individual exam project.

Menu:
1. Skapa tabeller
2. Lägg till testdata (idempotent)
3. Visa alla produkter
4. Visa produkter med tillverkare
5. Visa kunders orders
6. Visa topp-kunder (spending)
7. Nollställ databasen (DROP + CREATE)
8. Avsluta
"""

from exam_database import create_tables, reset_database
from populate_db import populate
import queries


def print_products(products):
    for p in products:
        print(f"- {p.id}: {p.name} ({p.category}) – {p.price} kr")


def print_products_with_brands(rows):
    for product, brand in rows:
        print(f"- {product.name} ({brand.name}) – {product.price} kr")


def print_customer_orders(rows):
    for order_id, first, last, total, status, date in rows:
        print(
            f"- Order {order_id}: {first} {last}, "
            f"{total} kr, {status}, {date}"
        )


def print_top_spenders(rows):
    for first, last, total in rows:
        print(f"- {first} {last}: {total} kr")


def print_products_with_ratings(rows):
    for name, avg_rating, num_reviews in rows:
        print(f"- {name}: {avg_rating} ({num_reviews} recensioner)")


def main():
    while True:
        print(
            """
================ Elektronikbutik - Meny ================
1. Skapa tabeller
2. Lägg till testdata (säkert, inga dubbletter)
3. Visa alla produkter
4. Visa produkter med tillverkare
5. Visa kunders orders
6. Visa toppkunder (spending)
7. Visa produkter med genomsnittligt betyg
8. Nollställ databasen (DROP + CREATE)
9. Avsluta
========================================================
"""
        )

        choice = input("Välj: ").strip()

        try:
            if choice == "1":
                create_tables()

            elif choice == "2":
                populate()

            elif choice == "3":
                print("\n Alla produkter:")
                prods = queries.get_all_products()
                print_products(prods)

            elif choice == "4":
                print("\n Produkter med tillverkare:")
                rows = queries.get_products_with_brands()
                print_products_with_brands(rows)

            elif choice == "5":
                print("\n Kunders orders:")
                rows = queries.get_customer_orders()
                print_customer_orders(rows)

            elif choice == "6":
                print("\n🏆 Toppkunder:")
                rows = queries.get_top_spenders()
                print_top_spenders(rows)

            elif choice == "7":
                print("\n Produkter med genomsnittligt betyg:")
                rows = queries.get_products_with_avg_rating()
                print_products_with_ratings(rows)

            elif choice == "8":
                confirm = input(
                    "Är du säker på att du vill nollställa databasen? (ja/nej): "
                ).strip().lower()
                if confirm == "ja":
                    reset_database()
                else:
                    print("Avbrutet.")

            elif choice == "9":
                print("Hejdå!")
                break

            else:
                print("Ogiltigt val, försök igen.")

        except KeyboardInterrupt:
            print("\nAvbrutet med Ctrl+C.")
        except Exception as e:
            print(f"\n Ett fel inträffade: {e}")


if __name__ == "__main__":
    main()