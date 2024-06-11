# 0x06. Python - Classes and Objects

## Overview

This project is dedicated to exploring the concepts of classes and objects in Python. Each task incrementally builds upon the previous one to create more complex structures and functionalities. Below are the detailed explanations for each task.

## Tasks

### 0. My First Square
**Objective**: Create an empty class `Square` that defines a square.

- **File**: `0-square.py`
- **Details**: This task introduces the basic concept of a class without any attributes or methods.

### 1. Square with Size
**Objective**: Enhance the `Square` class by adding a private instance attribute `size` and a constructor to initialize it.

- **File**: `1-square.py`
- **Details**: 
  - Private instance attribute: `size`
  - Instantiation with `size` (no type/value verification)

### 2. Size Validation
**Objective**: Extend the `Square` class to include size validation.

- **File**: `2-square.py`
- **Details**:
  - Private instance attribute: `size`
  - Instantiation with optional `size` parameter
  - Validate `size` to ensure it is an integer and non-negative

### 3. Area of a Square
**Objective**: Add a method to calculate the area of the square.

- **File**: `3-square.py`
- **Details**:
  - Private instance attribute: `size`
  - Method `def area(self):` that returns the area of the square

### 4. Access and Update Private Attribute
**Objective**: Implement getter and setter methods for the `size` attribute.

- **File**: `4-square.py`
- **Details**:
  - Getter method: `def size(self):` to retrieve `size`
  - Setter method: `def size(self, value):` to set `size`
  - Validate `size` in the setter method

### 5. Printing a Square
**Objective**: Add a method to print the square using the `#` character.

- **File**: `5-square.py`
- **Details**:
  - Method `def my_print(self):` to print the square
  - Prints an empty line if `size` is 0

### 6. Coordinates of a Square
**Objective**: Introduce the `position` attribute and modify the print method to consider position.

- **File**: `6-square.py`
- **Details**:
  - Private instance attribute: `position`
  - Getter method: `def position(self):` to retrieve `position`
  - Setter method: `def position(self, value):` to set `position`
  - Validate `position` to ensure it is a tuple of 2 positive integers
  - Adjust `my_print` to account for `position`

### 7. Singly Linked List
**Objective**: Create a `Node` class and a `SinglyLinkedList` class to manage nodes.

- **File**: `100-singly_linked_list.py`
- **Details**:
  - `Node` class with private attributes `data` and `next_node`
  - Getter and setter methods for `data` and `next_node`
  - `SinglyLinkedList` class with a private attribute `head`
  - Method to print the entire list
  - Method `def sorted_insert(self, value):` to insert nodes in sorted order

### 8. Print Square Instance
**Objective**: Modify the `Square` class to enable printing of its instance directly.

- **File**: `101-square.py`
- **Details**:
  - Ensure `Square` instance can be printed with the same behavior as `my_print`

### 9. Compare Two Squares
**Objective**: Implement comparison operators for the `Square` class based on the area.

- **File**: `102-square.py`
- **Details**:
  - Ensure `size` can be a float or integer
  - Implement comparison operators (`==`, `!=`, `>`, `>=`, `<`, `<=`)

### 10. ByteCode -> Python #5
**Objective**: Write a `MagicClass` that mimics the behavior of given Python bytecode.

- **File**: `103-magic_class.py`
- **Details**: Write a class `MagicClass` to match the provided bytecode.

