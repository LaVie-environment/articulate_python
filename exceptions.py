#!/usr/bin/env python3

try:
    int("a")
except ValueError as error:
    print(f"Something went wrong. Message: {error}")

print("Reached end of the program.")