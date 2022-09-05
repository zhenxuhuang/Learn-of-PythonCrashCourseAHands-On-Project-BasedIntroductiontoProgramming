# Python编程：从入门到实践
# 第4章 操作列表

# 4.3

# 第一种
squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(squares)

# 第二种
squares = [value**2 for value in range(1,11)]
print(squares)