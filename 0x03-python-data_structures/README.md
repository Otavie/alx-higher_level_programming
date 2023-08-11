# 0x03. PYTHON - DATA STRUCTURES: LISTS, TUPLES

This directory contains a collection of Python functions that focus on various list manipulation tasks. Each function is designed to accomplish a specific task related to **lists** and **tuples** and elements within them. The goal is to provide solutions to these tasks without relying on external modules or advanced language features.

## Task 0: Print a List of Integers

File: `print_list.py`

This function prints all integers from a given list, one integer per line. It adheres to the following requirements:
- Function Prototype: `def print_list_integer(my_list=[])`
- No external module is imported.
- Integers are printed using the `str.format()` method.

## Task 1: Secure Access to an Element in a List

File: `element_access.py`

This function retrieves an element from a list similar to the behavior in C. It follows the guidelines:
- Function Prototype: `def element_at(my_list, idx)`
- If `idx` is negative or out of range, `None` is returned.
- No external module is imported.
- No try/except constructs are used.

## Task 2: Replace Element in a List

File: `replace_element.py`

This function replaces an element in a list at a specified index, following the rules:
- Function Prototype: `def replace_in_list(my_list, idx, element)`
- If `idx` is negative or out of range, the original list is returned.
- No external module is imported.
- No try/except constructs are used.

## Task 3: Print a List of Integers in Reverse

File: `print_reverse_list.py`

This function prints all integers from a list in reverse order, adhering to the requirements:
- Function Prototype: `def print_reversed_list_integer(my_list=[])`
- No external module is imported.
- Integers are printed in reverse order using the `str.format()` method.

## Task 4: Replace Element in a Copy of the List

File: `replace_in_copy.py`

This function replaces an element in a copy of a list at a specified index, while considering the following conditions:
- Function Prototype: `def new_in_list(my_list, idx, element)`
- If `idx` is negative or out of range, a copy of the original list is returned.
- No external module is imported.
- No try/except constructs are used.

## Task 5: Remove 'c' and 'C' Characters from a String

File: `remove_c.py`

This function removes all occurrences of 'c' and 'C' characters from a given string, satisfying these criteria:
- Function Prototype: `def no_c(my_string)`
- The modified string with characters removed is returned.
- No external module is imported.
- The `str.replace()` method is not used.

## Task 6: Print a Matrix of Integers

File: `print_matrix.py`

This function prints a matrix of integers following the given format:
- Function Prototype: `def print_matrix_integer(matrix=[[]])`
- No external module is imported.
- Integers are printed using the `str.format()` method.

## Task 7: Add Two Tuples

File: `add_tuples.py`

This function adds two tuples element-wise according to the specifications:
- Function Prototype: `def add_tuple(tuple_a=(), tuple_b=())`
- A tuple containing the sum of the corresponding elements from both input tuples is returned.
- If a tuple has fewer than 2 elements, missing elements are considered 0.
- If a tuple has more than 2 elements, only the first 2 elements are used.
- No external module is imported.

## Task 8: Return String Length and First Character

File: `multiple_returns.py`

This function returns a tuple containing the length of a string and its first character, considering the following:
- Function Prototype: `def multiple_returns(sentence)`
- If the sentence is empty, the first character in the tuple is `None`.
- No external module is imported.

## Task 9: Find the Maximum Integer in a List

File: `max_integer.py`

This function finds the largest integer in a list as per the requirements:
- Function Prototype: `def max_integer(my_list=[])`
- If the list is empty, `None` is returned.
- No external module is imported.
- The built-in `max()` function is not used.

## Task 10: Identify Multiples of 2 in a List

File: `divisible_by_2.py`

This function identifies whether integers in a list are multiples of 2:
- Function Prototype: `def divisible_by_2(my_list=[])`
- A new list of boolean values is returned, where each value indicates if the corresponding integer in the original list is divisible by 2.
- No external module is imported.

## Task 11: Delete Item at Specific Position

File: `delete_at.py`

This function deletes an item at a specific position in a list based on these guidelines:
- Function Prototype: `def delete_at(my_list=[], idx=0)`
- If `idx` is negative or out of range, the list remains unchanged.
- The `pop()` method is not used.
- No external module is imported.

## Task 12: Switch Values of Two Variables

File: `switch_values.py`

This file contains source code with placeholders for switching the values of two variables (`a` and `b`). Your implementation should fit into the designated area and consist of exactly 5 lines of code.

## Task 13: Linked List Palindrome Check (C Function)

File: `linked_list_palindrome.c`

This C function checks if a singly linked list is a palindrome:
- Function Prototype: `int is_palindrome(listint_t **head)`
- Returns 0 if the linked list is not a palindrome and 1 if it is.
- An empty list is considered a palindrome.

## Contributors:
[Otavie Okuoyo](https://github.com/otavie)

## Date and Duration:
**Start Date:** Friday August 11, 2023 <br>
**First Deadline:** Monday August 15, 2023 <br>
**Duration:** 4 Days