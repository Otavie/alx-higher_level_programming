# 0x05. Python - Exceptions

This repository contains tasks focused on handling exceptions in Python. The exercises are designed to practice using `try` and `except` blocks to manage errors gracefully.

## Tasks

### 0. Safe List Printing

Write a function that prints `x` elements from a list.
- **Prototype**: `def safe_print_list(my_list=[], x=0):`
- The list can contain any type (integer, string, etc.).
- All elements must be printed on the same line followed by a new line.
- `x` represents the number of elements to print.
- `x` can be larger than the length of `my_list`.
- Returns the actual number of elements printed.
- Must use `try` and `except`.
- No imports allowed.
- Do not use `len()`.

**File**: `0-safe_print_list.py`

### 1. Safe Printing of an Integer List

Write a function that prints an integer using `"{:d}".format()`.
- **Prototype**: `def safe_print_integer(value):`
- `value` can be any type (integer, string, etc.).
- The integer should be printed followed by a new line.
- Returns `True` if `value` was printed correctly (i.e., it's an integer), otherwise returns `False`.
- Must use `try` and `except`.
- Must use `"{:d}".format()` to print as an integer.
- No imports allowed.
- Do not use `type()`.

**File**: `1-safe_print_integer.py`

### 2. Print and Count Integers

Write a function that prints the first `x` elements of a list, and only integers.
- **Prototype**: `def safe_print_list_integers(my_list=[], x=0):`
- The list can contain any type (integer, string, etc.).
- All integers must be printed on the same line followed by a new line; other types should be skipped silently.
- `x` represents the number of elements to access in `my_list`.
- `x` can be larger than the length of `my_list`, in which case an exception might occur.
- Returns the actual number of integers printed.
- Must use `try` and `except`.
- Must use `"{:d}".format()` to print an integer.
- No imports allowed.
- Do not use `len()`.

**File**: `2-safe_print_list_integers.py`

### 3. Integers Division with Debug

Write a function that divides two integers and prints the result.
- **Prototype**: `def safe_print_division(a, b):`
- Assumes `a` and `b` are integers.
- The result of the division should be printed in the `finally` section preceded by "Inside result:".
- Returns the result of the division, or `None` if division cannot be performed.
- Must use `try`, `except`, and `finally`.
- Must use `"{}".format()` to print the result.
- No imports allowed.

**File**: `3-safe_print_division.py`

### 4. Divide a List

Write a function that divides elements of two lists element by element.
- **Prototype**: `def list_division(my_list_1, my_list_2, list_length):`
- Both lists can contain any type (integer, string, etc.).
- `list_length` can be larger than the lengths of both lists.
- Returns a new list (length = `list_length`) with all divisions.
- If two elements cannot be divided, the result should be `0`.
  - If an element is not an integer or float: prints `wrong type`.
  - If division by zero occurs: prints `division by 0`.
  - If either list is too short: prints `out of range`.
- Must use `try`, `except`, and `finally`.
- No imports allowed.

**File**: `4-list_division.py`

### 5. Raise Exception

Write a function that raises a type exception.
- **Prototype**: `def raise_exception():`
- No imports allowed.

**File**: `5-raise_exception.py`

### 6. Raise a Message

Write a function that raises a name exception with a message.
- **Prototype**: `def raise_exception_msg(message=""):`
- No imports allowed.

**File**: `6-raise_exception_msg.py`

### 7. Safe Integer Print with Error Message

Write a function that prints an integer.
- **Prototype**: `def safe_print_integer_err(value):`
- `value` can be any type (integer, string, etc.).
- The integer should be printed followed by a new line.
- Returns `True` if `value` was printed correctly (i.e., it's an integer), otherwise returns `False` and prints the error to `stderr` preceded by "Exception:".
- Must use `try` and `except`.
- Must use `"{:d}".format()` to print as an integer.
- Do not use `type()`.

**File**: `100-safe_print_integer_err.py`

### 8. Safe Function

Write a function that executes another function safely.
- **Prototype**: `def safe_function(fct, *args):`
- Assumes `fct` will always be a function pointer.
- Returns the result of the function, or `None` if an error occurs and prints the error to `stderr` preceded by "Exception:".
- Must use `try` and `except`.

**File**: `101-safe_function.py`
