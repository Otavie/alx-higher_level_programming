#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        values_as_int = int(value)
        print("{:d}".format(value_as_int))
        return True
    except ValueError:
        print("Exception: ValueError occurred.", file=sys.stderr)
        return False
