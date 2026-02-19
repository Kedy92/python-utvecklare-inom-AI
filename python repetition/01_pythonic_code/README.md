# Python Repetition Course

This course is designed to review and strengthen Python fundamentals for students who need additional practice.

## 01. Pythonic Code

Watch all of his videos over time and you'll learn more:

https://www.youtube.com/@ArjanCodes

### How Python Works

**Interpreted Language**
- Python is interpreted, not compiled directly to machine code
- Source code (.py) -> Bytecode (.pyc in `__pycache__/`) -> Interpreter executes
- Errors are caught at runtime, not compile time

**Dynamically Typed**
- Variables don't have fixed types - they can hold any value
- `x = "hello"` then `x = 42` is perfectly valid
- This gives flexibility but requires discipline

**Duck Typing**
- "If it walks like a duck and quacks like a duck, it's a duck"
- Python cares about what an object can DO, not what type it IS
- A function accepting a "file" works with anything that has `.read()`

### Zen of Python

Open a python interpreter

```python
python

>>> import this

```

### PEP8

The Python style guide

https://peps.python.org/pep-0008/

### "We are all consenting adults"

Python has a unique culture compared to other languages. We believe in:

- **Trust over control** - Python has no real private variables. We use `_underscore` as convention, not enforcement. Developers trust each other.
- **Readability matters** - Code is read more often than it is written. Explicit is better than implicit.
- **Simplicity** - We don't overcomplicate. If something can be done simply, do it simply.
- **Type annotations** - We use type hints to make code more readable and explicit, not because Python requires it.

## 02. Functions, Methods & Error Handling

This section combines functions/methods with error handling - they go hand in hand. Good functions use proper error handling, and understanding error handling makes your functions more reusable.

### Error Handling Philosophy

**LBYL vs EAFP**
- **LBYL** (Look Before You Leap) - Check first, act second
- **EAFP** (Easier to Ask for Forgiveness than Permission) - Try it, handle errors if they occur

Both are pythonic - but they suit different situations.

**Raise - Let the caller handle the error**
- `raise` makes functions more reusable - the caller decides how to handle the error
- Return None/False only for binary situations
- Custom exceptions make it clearer what went wrong

**When to handle vs let it bubble up?**
- Sometimes the right answer is to NOT catch an exception - let it propagate upward
- This is an important part of writing reusable code

### Functions & Methods

- Functions should be slim and have a single responsibility
- Functions should NOT manipulate global variables - the `global` keyword is forbidden
- Use type annotations for parameters - it makes the code explicit and readable
- Functions should return values, not just print
- `raise` is an important tool - we signal errors to the caller instead of returning error codes

### Examples

The `bad/` folder contains examples of anti-patterns:
- Global variables and `global` keyword
- Functions that print instead of return
- Returning True/False instead of raising exceptions
- No type annotations

The `good/` folder contains the same programs written properly:
- Custom exceptions for clear error signaling
- Type annotations
- Single responsibility functions
- Local state instead of global

## 03. FastAPI Basics

Here we will practice error handling in a real context, use venvs, and write good helper functions for our endpoints.

### Setup

```bash
python -m venv venv
venv\\Scripts\\activate  # Windows
pip install fastapi uvicorn

```

### Topics

- Virtual environments in practice
- Endpoints and routing
- Path/query parameters
- Pydantic models for validation
- Error handling in endpoints (HTTPException, custom responses)
- Helper functions that raise exceptions

## 04. Git

### Topics

- git init, clone, status
- Staging and commits
- Branching and merging
- Remote repositories
- .gitignore

## Files Structure

```
repetition/
    README.md                     # This file
    01_pythonic_code/
        pythonic_code.ipynb       # Jupyter notebook
    02_functions_and_methods/
        functions_and_methods.ipynb
        bad/
            bad_functions.py      # Anti-patterns example
            bad_classes.py
        good/
            good_functions.py     # Proper patterns example
            good_classes.py
    03_fastapi_basics/
        main.py                   # FastAPI app
        requirements.txt
    04_git/
        README.md

```