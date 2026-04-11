#!/usr/bin/python3
def uppercase(number):
    for char in str:
        ascii=ord(char)
        if ascii >= 97 and ascii <= 122:
            char = chr(ascii-32)
        print("{}".format(char), end="")
    print("")
