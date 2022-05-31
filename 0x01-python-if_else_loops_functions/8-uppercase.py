#!/usr/bin/python3
def uppercase(str):
    for char in str:
        num = ord(char)
        print(f"{chr(num - 32) if 97 <= num <= 122 else char}", end="")
    print("")
