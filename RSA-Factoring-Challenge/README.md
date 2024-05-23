# RSA FACTORING CHALLENGE

This directory contains scripts for factorizing natural numbers into a product of two smaller numbers. The scripts are designed to work without any external dependencies and can handle large numbers efficiently.

## Task 0: Factorize Natural Numbers

### Usage
To factorize natural numbers, follow these steps:

1. Create a file containing the natural numbers you want to factorize.
2. Run the `factors` executable with the file as an argument.

```bash
./factors <file>
```

### Input
- The input file should contain one natural number per line.
- Each line should only contain the number and no additional characters.
- All numbers are guaranteed to be valid natural numbers greater than 1.

### Output
The program will output the factorization of each number in the format `n=p*q`, where `p` and `q` are two smaller numbers whose product is `n`.

## Task 1: RSA Factoring Challenge

In this advanced task, the goal is to factorize RSA numbers into two prime numbers. The scripts provided in this repository can efficiently factorize RSA numbers and find the two prime factors.

### Usage
To tackle the RSA Factoring Challenge:

1. Prepare a file containing the RSA numbers you want to factorize.
2. Run the `factors` executable with the file as an argument.

```bash
./factors <file>
```

### Input
- The input file should contain one RSA number per line.
- Each line should only contain the number and no additional characters.

### Output
The program will output the prime factorization of each RSA number. In this task, both factors `p` and `q` are guaranteed to be prime numbers.
