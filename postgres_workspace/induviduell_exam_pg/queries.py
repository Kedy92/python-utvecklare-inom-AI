# queries.py
"""
Python helper functions that run common queries against the electronics_db.
Used by exam_main.py to demonstrate SQL + ORM integration.
"""

from sqlalchemy import func
from exam_database import get_session
from exam_models import Brand, Product, Customer, Order, OrderItem, Review


def get_all_products():
    """Return all products sorted by name."""
    session = get_session()
    try:
        return (
            session.query(Product)
            .order_by(Product.name.asc())
            .all()
        )
    finally:
        session.close()


def get_products_over_price(min_price: float):
    """Return all products with price > min_price."""
    session = get_session()
    try:
        return (
            session.query(Product)
            .filter(Product.price > min_price)
            .order_by(Product.price.desc())
            .all()
        )
    finally:
        session.close()


def get_pending_orders():
    """Return all pending orders."""
    session = get_session()
    try:
        return session.query(Order).filter(Order.status == "pending").all()
    finally:
        session.close()


def get_products_with_brands():
    """Return (product, brand) tuples."""
    session = get_session()
    try:
        q = (
            session.query(Product, Brand)
            .join(Brand, Product.brand_id == Brand.id)
            .order_by(Brand.name, Product.name)
        )
        return q.all()
    finally:
        session.close()


def get_customer_orders():
    """Return orders with customer name and total amount."""
    session = get_session()
    try:
        q = (
            session.query(
                Order.id,
                Customer.first_name,
                Customer.last_name,
                Order.total_amount,
                Order.status,
                Order.order_date,
            )
            .join(Customer, Order.customer_id == Customer.id)
            .order_by(Order.order_date.desc())
        )
        return q.all()
    finally:
        session.close()


def get_top_spenders(limit: int = 5):
    """Return top customers by total spending."""
    session = get_session()
    try:
        q = (
            session.query(
                Customer.first_name,
                Customer.last_name,
                func.sum(Order.total_amount).label("total_spent"),
            )
            .join(Order, Order.customer_id == Customer.id)
            .group_by(Customer.id)
            .order_by(func.sum(Order.total_amount).desc())
            .limit(limit)
        )
        return q.all()
    finally:
        session.close()


def get_products_with_avg_rating():
    """Return products with their average rating."""
    session = get_session()
    try:
        q = (
            session.query(
                Product.name,
                func.round(func.avg(Review.rating), 2).label("avg_rating"),
                func.count(Review.id).label("num_reviews"),
            )
            .join(Review, Review.product_id == Product.id)
            .group_by(Product.id)
            .order_by(func.avg(Review.rating).desc())
        )
        return q.all()
    finally:
        session.close()