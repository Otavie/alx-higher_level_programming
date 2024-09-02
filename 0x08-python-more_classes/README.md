# 0x08. Python - More Classes and Objects

This repository contains a series of tasks that focus on deepening your understanding of object-oriented programming in Python, particularly through the use of classes and objects. The exercises range from defining simple classes to implementing more complex functionality like static methods, class methods, and special methods for string representation.

## Table of Contents

1. [Simple Rectangle](#simple-rectangle)
2. [Real Definition of a Rectangle](#real-definition-of-a-rectangle)
3. [Area and Perimeter](#area-and-perimeter)
4. [String Representation](#string-representation)
5. [Eval is Magic](#eval-is-magic)
6. [Detect Instance Deletion](#detect-instance-deletion)
7. [How Many Instances](#how-many-instances)
8. [Change Representation](#change-representation)
9. [Compare Rectangles](#compare-rectangles)
10. [A Square is a Rectangle](#a-square-is-a-rectangle)
11. [N Queens](#n-queens)

## Simple Rectangle

**File:** `0-rectangle.py`

Defines an empty class `Rectangle` that represents a rectangle. The class contains no methods or attributes.

## Real Definition of a Rectangle

**File:** `1-rectangle.py`

Enhances the `Rectangle` class by adding private instance attributes for `width` and `height`. These attributes have getter and setter methods, and the setters include validation to ensure that the values are integers greater than or equal to zero.

## Area and Perimeter

**File:** `2-rectangle.py`

This task adds methods to calculate the area and perimeter of the rectangle. The area is simply `width * height`, and the perimeter is `2 * (width + height)`, but if either dimension is zero, the perimeter is also zero.

## String Representation

**File:** `3-rectangle.py`

Implements the `__str__` method to provide a string representation of the rectangle using the `#` character. If either the width or height is zero, it returns an empty string.

## Eval is Magic

**File:** `4-rectangle.py`

Adds a `__repr__` method to the `Rectangle` class, allowing for the recreation of the rectangle object using `eval()`. The method returns a string that resembles the constructor call used to create the instance.

## Detect Instance Deletion

**File:** `5-rectangle.py`

Introduces a `__del__` method that prints a message when a `Rectangle` instance is deleted. This provides a way to detect when objects are garbage collected.

## How Many Instances

**File:** `6-rectangle.py`

Introduces a class attribute `number_of_instances` that keeps track of the number of `Rectangle` instances created and deleted. This attribute is incremented during instantiation and decremented upon deletion.

## Change Representation

**File:** `7-rectangle.py`

Extends the `Rectangle` class by adding a class attribute `print_symbol`, which is used to customize the character(s) used in the string representation of the rectangle.

## Compare Rectangles

**File:** `8-rectangle.py`

Adds a static method `bigger_or_equal` that compares two `Rectangle` instances and returns the one with the larger area. If both have the same area, it returns the first instance.

## A Square is a Rectangle

**File:** `9-rectangle.py`

Adds a class method `square` that returns a new `Rectangle` instance where both the width and height are equal, effectively creating a square.

## N Queens

**File:** `101-nqueens.py`

Implements a program to solve the N Queens problem, which involves placing N non-attacking queens on an N×N chessboard. The program prints all possible solutions, where each solution is a list of queen positions on the board.

