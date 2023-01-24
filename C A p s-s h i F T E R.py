#!/bin/python
import random

message: str = input("Message > ")

print("\n")

for i in message:
    a = random.randint(0,1)
    if a == 0:
        print(i.lower(), end=" ")
    
    if a == 1:
        print(i.upper(), end=" ")

