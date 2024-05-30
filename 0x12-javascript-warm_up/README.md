# JavaScript Tasks

This repository contains a series of JavaScript tasks to help you practice and understand various JavaScript concepts. Each task is implemented in a separate script file as specified below.

## Table of Contents

0. [First constant, first print](#0-first-constant-first-print)
1. [3 languages](#1-3-languages)
2. [Arguments](#2-arguments)
3. [Value of my argument](#3-value-of-my-argument)
4. [Create a sentence](#4-create-a-sentence)
5. [An Integer](#5-an-integer)
6. [Loop to languages](#6-loop-to-languages)
7. [I love C](#7-i-love-c)
8. [Square](#8-square)
9. [Add](#9-add)
10. [Factorial](#10-factorial)
11. [Second biggest!](#11-second-biggest)
12. [Object](#12-object)
13. [Add file](#13-add-file)
14. [Const or not const](#14-const-or-not-const)
15. [Call me Moby](#15-call-me-moby)
16. [Add me maybe](#16-add-me-maybe)
17. [Increment object](#17-increment-object)

## Tasks

### 0. First constant, first print
Write a script that prints "JavaScript is amazing":
- Create a constant variable called `myVar` with the value "JavaScript is amazing"
- Use `console.log(...)` to print the output
- You are not allowed to use `var`
- **File:** `0-javascript_is_amazing.js`

### 1. 3 languages
Write a script that prints 3 lines:
- The first line: "C is fun"
- The second line: "Python is cool"
- The third line: "JavaScript is amazing"
- Use `console.log(...)` to print all output
- You are not allowed to use `var`
- **File:** `1-multi_languages.js`

### 2. Arguments
Write a script that prints a message depending on the number of arguments passed:
- If no arguments are passed to the script, print "No argument"
- If only one argument is passed to the script, print "Argument found"
- Otherwise, print "Arguments found"
- Use `console.log(...)` to print all output
- You are not allowed to use `var`
- Reference: `process.argv`
- **File:** `2-arguments.js`

### 3. Value of my argument
Write a script that prints the first argument passed to it:
- If no arguments are passed to the script, print "No argument"
- Use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `length`
- **File:** `3-value_argument.js`

### 4. Create a sentence
Write a script that prints two arguments passed to it, in the following format: " is "
- Use `console.log(...)` to print all output
- You are not allowed to use `var`
- **File:** `4-concat.js`

### 5. An Integer
Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:
- If the argument can’t be converted to an integer, print "Not a number"
- Use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `try/catch`
- **File:** `5-to_integer.js`

### 6. Loop to languages
Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
- The first line: "C is fun"
- The second line: "Python is cool"
- The third line: "JavaScript is amazing"
- Use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use any `if/else` statement
- You can use only one `console.log`
- You must use a loop (while, for, etc.)
- **File:** `6-multi_languages_loop.js`

### 7. I love C
Write a script that prints `x` times "C is fun"
- Where `x` is the first argument of the script
- If the first argument can’t be converted to an integer, print "Missing number of occurrences"
- Use `console.log(...)` to print all output
- You are not allowed to use `var`
- You can use only two `console.log`
- You must use a loop (while, for, etc.)
- **File:** `7-multi_c.js`

### 8. Square
Write a script that prints a square
- The first argument is the size of the square
- If the first argument can’t be converted to an integer, print "Missing size"
- You must use the character `X` to print the square
- Use `console.log(...)` to print all output
- You are not allowed to use `var`
- You must use a loop (while, for, etc.)
- **File:** `8-square.js`

### 9. Add
Write a script that prints the addition of 2 integers
- The first argument is the first integer
- The second argument is the second integer
- You have to define a function with this prototype: `function add(a, b)`
- Use `console.log(...)` to print all output
- You are not allowed to use `var`
- **File:** `9-add.js`

### 10. Factorial
Write a script that computes and prints a factorial
- The first argument is an integer (argument can be cast as integer) used for computing the factorial
- Factorial of `NaN` is `1`
- You must do it recursively
- You must use a function
- Use `console.log(...)` to print all output
- You are not allowed to use `var`
- **File:** `10-factorial.js`

### 11. Second biggest!
Write a script that searches the second biggest integer in the list of arguments.
- You can assume all arguments can be converted to integer
- If no argument passed, print `0`
- If the number of arguments is `1`, print `0`
- Use `console.log(...)` to print all output
- You are not allowed to use `var`
- **File:** `11-second_biggest.js`

### 12. Object
Update this script to replace the value `12` with `89`:
- You are not allowed to use `var`
- **File:** `12-object.js`

### 13. Add file
Write a function that returns the addition of 2 integers.
- The function must be visible from outside
- The name of the function must be `add`
- You are not allowed to use `var`
- **File:** `13-add.js`

### 14. Const or not const
Write a file that modifies the value of `myVar` to `333`
- **File:** `100-let_me_const.js`

### 15. Call me Moby
Write a function that executes `x` times a function.
- The function must be visible from outside
- Prototype: `function (x, theFunction)`
- You are not allowed to use `var`
- **File:** `101-call_me_moby.js`

### 16. Add me maybe
Write a function that increments and calls a function.
- The function must be visible from outside
- Prototype: `function (number, theFunction)`
- You are not allowed to use `var`
- **File:** `102-add_me_maybe.js`

### 17. Increment object
Update this script by adding a new function `incr` that increments the integer value.
- You are not allowed to use `var`
- **File:** `103-object_fct.js`
