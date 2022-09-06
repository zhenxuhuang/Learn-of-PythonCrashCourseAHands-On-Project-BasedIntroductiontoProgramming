# Python编程：从入门到实践
# 第7章 用户输入和while循环
# 7.1
number = int(input("Enter a number, and I'll tell you if it's even or odd: "))

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
