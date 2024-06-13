#!/usr/bin/python3
"""Creates class MyList"""


class MyList(list):
    """A class MyLIst that inherits from list"""

    def print_sorted(self):
        """Public instance method that printed sorted list"""
        
        self.sort()
        print(self)
