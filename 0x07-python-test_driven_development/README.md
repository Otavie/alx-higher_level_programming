# 0x07. Python - Test-driven Development

## Tasks

### 0. Integers Addition

Write a function that adds 2 integers.

- **Prototype**: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats; otherwise, raise a `TypeError` with the message `a must be an integer` or `b must be an integer`.
- Convert `a` and `b` to integers if they are floats.
- Returns an integer: the sum of `a` and `b`.
- No module imports allowed.

**File**: `0-add_integer.py`, `tests/0-add_integer.txt`

### 1. Divide a Matrix

Write a function that divides all elements of a matrix.

- **Prototype**: `def matrix_divided(matrix, div):`
- `matrix` must be a list of lists of integers or floats; otherwise, raise a `TypeError` with the message `matrix must be a matrix (list of lists) of integers/floats`.
- Each row of the matrix must be of the same size; otherwise, raise a `TypeError` with the message `Each row of the matrix must have the same size`.
- `div` must be a number (integer or float); otherwise, raise a `TypeError` with the message `div must be a number`.
- `div` cannot be 0; otherwise, raise a `ZeroDivisionError` with the message `division by zero`.
- All elements of the matrix should be divided by `div`, rounded to 2 decimal places.
- Returns a new matrix.
- No module imports allowed.

**File**: `2-matrix_divided.py`, `tests/2-matrix_divided.txt`

### 2. Say My Name

Write a function that prints "My name is `<first name>` `<last name>`".

- **Prototype**: `def say_my_name(first_name, last_name=""):`
- `first_name` and `last_name` must be strings; otherwise, raise a `TypeError` with the message `first_name must be a string` or `last_name must be a string`.
- No module imports allowed.

**File**: `3-say_my_name.py`, `tests/3-say_my_name.txt`

### 3. Print Square

Write a function that prints a square with the character `#`.

- **Prototype**: `def print_square(size):`
- `size` must be an integer; otherwise, raise a `TypeError` with the message `size must be an integer`.
- If `size` is less than 0, raise a `ValueError` with the message `size must be >= 0`.
- If `size` is a float and is less than 0, raise a `TypeError` with the message `size must be an integer`.
- No module imports allowed.

**File**: `4-print_square.py`, `tests/4-print_square.txt`

### 4. Text Indentation

Write a function that prints text with 2 new lines after each of these characters: `.`, `?`, and `:`.

- **Prototype**: `def text_indentation(text):`
- `text` must be a string; otherwise, raise a `TypeError` with the message `text must be a string`.
- No space should be present at the beginning or end of each printed line.
- No module imports allowed.

**File**: `5-text_indentation.py`, `tests/5-text_indentation.txt`

### 5. Max Integer - Unittest

Add unittests for the function `def max_integer(list=[])`.

- Your test file should be inside a folder `tests`.
- Use the `unittest` module.
- Your test file should be Python files (extension: .py).
- Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`.
- All tests you write must be passable by the function.
- Collaboration on test cases is encouraged to cover all edge cases.

**File**: `tests/6-max_integer_test.py`

### 6. Matrix Multiplication

Write a function that multiplies 2 matrices.

- **Prototype**: `def matrix_mul(m_a, m_b):`
- Validate `m_a` and `m_b` with these requirements:
  - `m_a` and `m_b` must be a list of lists of integers or floats.
  - If `m_a` or `m_b` is not a list, raise a `TypeError` with the message `m_a must be a list` or `m_b must be a list`.
  - If `m_a` or `m_b` is not a list of lists, raise a `TypeError` with the message `m_a must be a list of lists` or `m_b must be a list of lists`.
  - If `m_a` or `m_b` is empty (i.e., `[]` or `[[]]`), raise a `ValueError` with the message `m_a can't be empty` or `m_b can't be empty`.
  - If any element of those list of lists is not an integer or a float, raise a `TypeError` with the message `m_a should contain only integers or floats` or `m_b should contain only integers or floats`.
  - If `m_a` or `m_b` is not a rectangle (all rows should be of the same size), raise a `TypeError` with the message `each row of m_a must be of the same size` or `each row of m_b must be of the same size`.
  - If `m_a` and `m_b` can't be multiplied, raise a `ValueError` with the message `m_a and m_b can't be multiplied`.
- No module imports allowed.

**File**: `100-matrix_mul.py`, `tests/100-matrix_mul.txt`

### 7. Lazy Matrix Multiplication

Write a function that multiplies 2 matrices using the `NumPy` module.

- To install `NumPy`: `pip3 install numpy==1.15.0`.
- **Prototype**: `def lazy_matrix_mul(m_a, m_b):`
- Test cases should be the same as `100-matrix_mul` but with a new exception type/message.

**File**: `101-lazy_matrix_mul.py`, `tests/101-lazy_matrix_mul.txt`

### 8. CPython #3: Python Strings

Create a function that prints Python strings.

- **Prototype**: `void print_python_string(PyObject *p);`
- Format: see example.
- If `p` is not a valid string, print an error message (see example).
- Read: Unicode HOWTO.
- Python version: 3.4.
- You are allowed to use the C standard library.
- Your shared library will be compiled with this command line: `gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c`.

**File**: `102-python.c`
