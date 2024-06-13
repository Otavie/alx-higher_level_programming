### Tasks for "0x0A. Python - Inheritance"

**Task 0: Lookup**

Write a function `lookup` in `0-lookup.py` that returns the list of available attributes and methods of an object.

**Task 1: My list**

Write a class `MyList` in `1-my_list.py` that inherits from `list`. It should have a public instance method `print_sorted()` that prints the list in ascending order.

**Task 2: Exact same object**

Write a function `is_same_class` in `2-is_same_class.py` that returns `True` if an object is exactly an instance of a specified class; otherwise `False`.

**Task 3: Same class or inherit from**

Write a function `is_kind_of_class` in `3-is_kind_of_class.py` that returns `True` if an object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.

**Task 4: Only sub class of**

Write a function `inherits_from` in `4-inherits_from.py` that returns `True` if an object is an instance of a class that inherited (directly or indirectly) from a specified class; otherwise `False`.

**Task 5: Geometry module**

Write an empty class `BaseGeometry` in `5-base_geometry.py`.

**Task 6: Improve Geometry**

Enhance the `BaseGeometry` class from Task 5 (`6-base_geometry.py`) with a public instance method `area()` that raises an Exception with the message "area() is not implemented".

**Task 7: Integer validator**

Extend the `BaseGeometry` class from Task 6 (`7-base_geometry.py`) with:
- The existing `area()` method that raises an Exception with the message "area() is not implemented".
- A public instance method `integer_validator(self, name, value)` that validates `value`:
  - Raises a `TypeError` if `value` is not an integer with the message `<name> must be an integer`.
  - Raises a `ValueError` if `value` is less than or equal to 0 with the message `<name> must be greater than 0`.

**Task 8: Rectangle**

Write a class `Rectangle` in `8-rectangle.py` that inherits from `BaseGeometry` (from Task 7):
- Instantiates with private attributes `width` and `height`.
- Validates `width` and `height` using `integer_validator`.
- Ensures no getter or setter for `width` and `height`.

**Task 9: Full rectangle**

Write a class `Rectangle` in `9-rectangle.py` that inherits from `BaseGeometry` (from Task 7):
- Instantiates with private attributes `width` and `height`.
- Validates `width` and `height` using `integer_validator`.
- Implements `area()` method.
- Defines `print()` to print `[Rectangle] <width>/<height>`.

**Task 10: Square #1**

Write a class `Square` in `10-square.py` that inherits from `Rectangle` (from Task 9):
- Instantiates with private attribute `size`.
- Validates `size` using `integer_validator`.
- Implements `area()` method.

**Task 11: Square #2**

Write a class `Square` in `11-square.py` that inherits from `Rectangle` (from Task 9):
- Instantiates with private attribute `size`.
- Validates `size` using `integer_validator`.
- Implements `area()` method.
- Defines `print()` to print `[Square] <width>/<height>`.

**Task 12: My integer (Advanced)**

Write a class `MyInt` in `100-my_int.py` that inherits from `int`:
- Reverses the behavior of `==` and `!=` operators.

**Task 13: Can I? (Advanced)**

Write a function `add_attribute` in `101-add_attribute.py` that adds a new attribute to an object if possible; otherwise raises a `TypeError` with the message "can't add new attribute".
