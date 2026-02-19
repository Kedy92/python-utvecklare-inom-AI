# exam_models.py
"""
Databasmodeller - importerar Base från exam_database.py
"""
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DECIMAL,
    Date,
    TIMESTAMP,
    ForeignKey,
    CheckConstraint,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from exam_database import Base  # <-- Importerar Base från exam_database.py


class Brand(Base):
    """Tillverkare"""
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    country = Column(String(100))
    founded_year = Column(Integer)
    description = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.now)

    products = relationship(
        "Product", back_populates="brand", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Brand(name='{self.name}')>"


class Product(Base):
    """Produkter"""
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    brand_id = Column(
        Integer, ForeignKey("brands.id", ondelete="CASCADE"), nullable=False
    )
    sku = Column(String(50), unique=True)
    release_year = Column(Integer)
    price = Column(DECIMAL(10, 2), nullable=False)
    warranty_months = Column(Integer)
    category = Column(String(50))
    stock_quantity = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, default=datetime.now)

    __table_args__ = (
        CheckConstraint("price > 0", name="check_price_positive"),
        CheckConstraint("stock_quantity >= 0", name="check_stock_non_negative"),
    )

    brand = relationship("Brand", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product")
    reviews = relationship("Review", back_populates="product")

    def __repr__(self):
        return f"<Product(name='{self.name}', price={self.price})>"


class Customer(Base):
    """Kunder"""
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    phone = Column(String(20))
    city = Column(String(100))
    registration_date = Column(Date, default=datetime.now().date)
    created_at = Column(TIMESTAMP, default=datetime.now)

    orders = relationship("Order", back_populates="customer")
    reviews = relationship("Review", back_populates="customer")

    def __repr__(self):
        return f"<Customer(name='{self.first_name} {self.last_name}')>"


class Order(Base):
    """Beställningar"""
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    customer_id = Column(
        Integer, ForeignKey("customers.id", ondelete="CASCADE"), nullable=False
    )
    order_date = Column(Date, default=datetime.now().date)
    total_amount = Column(DECIMAL(10, 2))
    status = Column(String(20), default="pending")
    shipping_city = Column(String(100))
    created_at = Column(TIMESTAMP, default=datetime.now)

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship(
        "OrderItem", back_populates="order", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Order(id={self.id}, status='{self.status}')>"


class OrderItem(Base):
    """Beställningsrader"""
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(
        Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False
    )
    product_id = Column(
        Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False
    )
    quantity = Column(Integer, nullable=False)
    unit_price = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now)

    __table_args__ = (
        CheckConstraint("quantity > 0", name="check_quantity_positive"),
        CheckConstraint("unit_price > 0", name="check_unit_price_positive"),
    )

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")

    def __repr__(self):
        return f"<OrderItem(product_id={self.product_id}, qty={self.quantity})>"


class Review(Base):
    """Recensioner"""
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    product_id = Column(
        Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False
    )
    customer_id = Column(
        Integer, ForeignKey("customers.id", ondelete="CASCADE"), nullable=False
    )
    rating = Column(Integer)
    comment = Column(Text)
    review_date = Column(Date, default=datetime.now().date)
    created_at = Column(TIMESTAMP, default=datetime.now)

    __table_args__ = (
        CheckConstraint("rating >= 1 AND rating <= 5", name="check_rating_range"),
    )

    product = relationship("Product", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    def __repr__(self):
        return f"<Review(product_id={self.product_id}, rating={self.rating})>"