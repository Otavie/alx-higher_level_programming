#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError:
        print("Exception: ValueError occurred.", file=sys.stderr)
        return false
