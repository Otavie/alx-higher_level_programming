# 0x04. Python - More Data Structures: Set, Dictionary

This repository contains various tasks that involve working with Python's data structures such as sets and dictionaries. Below is a detailed explanation of each task, its requirements, and the expected outcomes.

## Tasks

### 0. Squared simple
Create a function that calculates the square of every integer in a 2D matrix.

- **Prototype:** `def square_matrix_simple(matrix=[]):`
- **Input:** A 2-dimensional list `matrix`
- **Output:** A new matrix with the same dimensions where each value is squared
- **Restrictions:** 
  - Do not modify the original matrix
  - Do not import any modules
  - You may use loops and functions like `map`
- **File:** `0-square_matrix_simple.py`

### 1. Search and replace
Create a function that substitutes all occurrences of a specific element in a list with another element.

- **Prototype:** `def search_replace(my_list, search, replace):`
- **Parameters:**
  - `my_list`: The original list
  - `search`: The element to be replaced
  - `replace`: The new element to replace the `search`
- **Restrictions:** Do not import any modules
- **File:** `1-search_replace.py`

### 2. Unique addition
Create a function that sums all unique integers in a list, ensuring each integer is added only once.

- **Prototype:** `def uniq_add(my_list=[]):`
- **Restrictions:** Do not import any modules
- **File:** `2-uniq_add.py`

### 3. Present in both
Create a function that returns a set containing elements that are common to two sets.

- **Prototype:** `def common_elements(set_1, set_2):`
- **Restrictions:** Do not import any modules
- **File:** `3-common_elements.py`

### 4. Only differents
Create a function that returns a set containing elements that are in either of the two sets but not in both.

- **Prototype:** `def only_diff_elements(set_1, set_2):`
- **Restrictions:** Do not import any modules
- **File:** `4-only_diff_elements.py`

### 5. Number of keys
Create a function that counts the number of keys in a dictionary.

- **Prototype:** `def number_keys(a_dictionary):`
- **Restrictions:** Do not import any modules
- **File:** `5-number_keys.py`

### 6. Print sorted dictionary
Create a function that prints a dictionary with its keys sorted alphabetically.

- **Prototype:** `def print_sorted_dictionary(a_dictionary):`
- **Assumptions:** 
  - All keys are strings
  - Sort only the first-level keys
  - Dictionary values can be of any type
- **Restrictions:** Do not import any modules
- **File:** `6-print_sorted_dictionary.py`

### 7. Update dictionary
Create a function that adds or updates a key/value pair in a dictionary.

- **Prototype:** `def update_dictionary(a_dictionary, key, value):`
- **Parameters:**
  - `key`: Always a string
  - `value`: Can be of any type
- **Behavior:**
  - Replace value if key exists
  - Add key/value pair if key does not exist
- **Restrictions:** Do not import any modules
- **File:** `7-update_dictionary.py`

### 8. Simple delete by key
Create a function that removes a key from a dictionary.

- **Prototype:** `def simple_delete(a_dictionary, key=""):`
- **Parameters:**
  - `key`: Always a string
- **Behavior:** If the key does not exist, do not modify the dictionary
- **Restrictions:** Do not import any modules
- **File:** `8-simple_delete.py`

### 9. Multiply by 2
Create a function that returns a new dictionary with all values multiplied by 2.

- **Prototype:** `def multiply_by_2(a_dictionary):`
- **Assumptions:** All values are integers
- **Restrictions:** Do not import any modules
- **File:** `9-multiply_by_2.py`

### 10. Best score
Create a function that returns the key with the highest integer value in a dictionary.

- **Prototype:** `def best_score(a_dictionary):`
- **Assumptions:** 
  - All values are integers
  - If no scores are found, return `None`
  - Each student has a unique score
- **Restrictions:** Do not import any modules
- **File:** `10-best_score.py`

### 11. Multiply by using map
Create a function that returns a list where all values are multiplied by a given number without using loops.

- **Prototype:** `def multiply_list_map(my_list=[], number=0):`
- **Output:** A new list with the same length where each value is multiplied by `number`
- **Restrictions:** 
  - Do not modify the initial list
  - Do not import any modules
  - Must use `map`
  - The file should not exceed 3 lines
- **File:** `11-multiply_list_map.py`

### 12. Roman to Integer
Prepare for technical interviews by creating a function to convert Roman numerals to integers.

- **Prototype:** `def roman_to_int(roman_string):`
- **Assumptions:** 
  - The number is between 1 and 3999
  - If the input is not a string or is `None`, return 0
- **File:** `12-roman_to_int.py`

### 13. Weighted average!
Create a function that calculates the weighted average of integers from tuples in the format `(score, weight)`.

- **Prototype:** `def weight_average(my_list=[]):`
- **Output:** 0 if the list is empty
- **Restrictions:** Do not import any modules
- **File:** `100-weight_average.py`

### 14. Squared by using map
Create a function that computes the square of all integers in a 2D matrix using `map`.

- **Prototype:** `def square_matrix_map(matrix=[]):`
- **Output:** A new matrix with the same dimensions where each value is squared
- **Restrictions:** 
  - Do not modify the initial matrix
  - Do not import any modules
  - Must use `map`
  - Do not use `for` or `while`
  - The file should not exceed 3 lines
- **File:** `101-square_matrix_map.py`

### 15. Delete by value
Create a function that removes keys with a specific value from a dictionary.

- **Prototype:** `def complex_delete(a_dictionary, value):`
- **Behavior:** If the value does not exist, the dictionary remains unchanged
- **Restrictions:** Do not import any modules
- **File:** `102-complex_delete.py`

### 16. CPython #1: PyBytesObject
Create two C functions to display basic information about Python lists and bytes objects.

- **Python Lists:**
  - **Prototype:** `void print_python_list(PyObject *p);`
  - **Format:** Refer to the example provided
- **Python Bytes:**
  - **Prototype:** `void print_python_bytes(PyObject *p);`
  - **Format:** Refer to the example provided
  - **Line “first X bytes”**: Print a maximum of 10 bytes
  - **Error Handling:** If `p` is not a valid `PyBytesObject`, print an error message
  - **File:** `103-python.c`
- **Compilation:**
  - Command: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c`
  - **Restrictions:**
    - Do not use `Py_SIZE`, `Py_TYPE`, `PyList_GetItem`, `PyBytes_AS_STRING`, or `PyBytes_GET_SIZE`
- **Python Version:** 3.4
