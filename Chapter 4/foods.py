# Python编程：从入门到实践
# 第4章 操作列表

# 4.4
my_foods = ['pizza', 'falafel', 'carrot cake']
# python中切片是将副本复制
# 若不切片直接相等，即此处为friend_foods = my_foods，则类似于指针指向同一地址
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)