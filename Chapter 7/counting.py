# Python编程：从入门到实践
# 第7章 用户输入和while循环
# 7.2
"""current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
"""

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
