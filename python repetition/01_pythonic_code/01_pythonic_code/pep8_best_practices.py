"""
PEP8 - Python's Style Guide

These aren't just formatting rules. They're about making code readable.
"Code is read more often than it is written."

Full guide: https://peps.python.org/pep-0008/
"""

# =============================================================================
# NAMING CONVENTIONS
# =============================================================================

# Variables and functions: snake_case
user_name = "alice"
total_amount = 150.50

def calculate_tax(amount: float, rate: float) -> float:
    return amount * rate


# Classes: PascalCase
class UserAccount:
    pass

class HTTPRequestHandler:  # Acronyms stay uppercase
    pass


# Constants: UPPER_SNAKE_CASE
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30
DATABASE_URL = "postgresql://localhost/db"


# Protected/Private: leading underscore(s)
class Example:
    def __init__(self):
        self._internal_state = None      # Protected
        self.__very_private = None       # Private (name mangled)

    def _helper_method(self):            # Protected method
        pass


# =============================================================================
# IMPORTS - Order matters
# =============================================================================

# 1. Standard library imports
import os
import sys
from datetime import datetime
from typing import Optional

# 2. Third-party imports (blank line between groups)
# import requests
# import pandas as pd
# from fastapi import FastAPI

# 3. Local application imports (blank line between groups)
# from .models import User
# from .database import get_connection


# Bad: mixing import styles, no grouping
# import os, sys, requests, pandas  # Don't do this


# =============================================================================
# WHITESPACE AND FORMATTING
# =============================================================================

# Good: spaces around operators
result = 5 + 3
is_valid = x == y
total = price * quantity

# Bad: inconsistent or no spaces
# result=5+3
# is_valid=x==y

# Good: no space before colon in slices and dicts
my_list = [1, 2, 3, 4, 5]
subset = my_list[1:3]
config = {"key": "value", "count": 42}

# Good: space after comma, not before
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age}"

# Bad:
# def greet(name:str ,age:int)->str:


# =============================================================================
# LINE LENGTH AND BREAKING
# =============================================================================

# PEP8 recommends 79 characters, many teams use 88-120
# The point: be consistent in your project

# Good: break long lines logically
def create_user(
    username: str,
    email: str,
    password: str,
    is_admin: bool = False
) -> dict:
    return {
        "username": username,
        "email": email,
        "is_admin": is_admin
    }


# Good: break long conditions
def is_valid_order(order: dict) -> bool:
    has_items = len(order.get("items", [])) > 0
    has_customer = order.get("customer_id") is not None
    is_not_cancelled = order.get("status") != "cancelled"

    return has_items and has_customer and is_not_cancelled


# Bad: one massive line
# def is_valid_order(order): return len(order.get("items", [])) > 0 and order.get("customer_id") is not None and order.get("status") != "cancelled"


# =============================================================================
# COMPARISONS
# =============================================================================

# Use 'is' for None, True, False
if result is None:
    print("No result")

if is_active is True:  # Or just: if is_active:
    print("Active")


# Use '==' for value comparison
if status == "pending":
    print("Waiting...")

if count == 0:  # Not: count is 0
    print("Empty")


# Truthiness - Pythonic way
items = []

# Good: rely on truthiness
if not items:
    print("List is empty")

if items:
    print("List has items")

# Also fine, but more verbose
if len(items) == 0:
    print("List is empty")


# =============================================================================
# TYPE ANNOTATIONS - Modern Python
# =============================================================================

# Type hints make code more readable and explicit
# They don't enforce anything at runtime - another "consenting adults" thing

def get_user_by_id(user_id: int) -> Optional[dict]:
    """
    Type hints tell other developers:
    - This function expects an int
    - It returns either a dict or None
    """
    users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    return users.get(user_id)


def process_items(items: list[str], limit: int = 10) -> list[str]:
    """
    Modern syntax (Python 3.9+): list[str] instead of List[str]
    """
    return items[:limit]


# Type hints for class attributes
class Product:
    name: str
    price: float
    in_stock: bool

    def __init__(self, name: str, price: float, in_stock: bool = True):
        self.name = name
        self.price = price
        self.in_stock = in_stock


# =============================================================================
# DOCSTRINGS
# =============================================================================

def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate the discounted price.

    Args:
        price: The original price
        discount_percent: Discount as a percentage (0-100)

    Returns:
        The price after discount

    Raises:
        ValueError: If discount_percent is negative or > 100
    """
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")

    discount = price * (discount_percent / 100)
    return price - discount


# =============================================================================
# THE TAKEAWAY
# =============================================================================

"""
PEP8 is about communication:

1. Naming tells you what something IS (constant, class, function, protected)
2. Formatting makes code scannable
3. Type hints clarify intent
4. Docstrings explain behavior

Consistency matters more than any single rule.
Pick a style, stick to it.

Tools that help:
- black (auto-formatter)
- ruff (linter, very fast)
- mypy (type checker)
"""
