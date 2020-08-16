"""
Test imports from the package itself.
"""
import random


def get_string_options():
    return ['STRONG'] * random.randint(2, 10) + \
           ['NORMAL'] * random.randint(1, 10) + \
           ['WEAK'] * random.randint(5, 10)
