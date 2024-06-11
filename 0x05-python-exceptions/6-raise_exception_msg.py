#!/usr/bin/python3

def raise_exception_msg(message=""):
    class NameException(Exception):
        pass
    if not message:
        message = "Name exception occurred."
    raise NameException(message)
