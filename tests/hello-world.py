#! /usr/bin/env python

import email
import sys

print(str("hello", "utf8"), str("world!", "ascii"))

print("sys.path:", sys.path)
print("__file__:", __file__)
print("__name__:", __name__)

print("locals():", locals())

print("sys.argv", sys.argv)
print("sys.executable:", sys.executable)
