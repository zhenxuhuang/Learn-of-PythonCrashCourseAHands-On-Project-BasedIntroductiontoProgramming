"""
Python编程：从入门到实践
第7章 用户输入和while循环

7.1
"""

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
