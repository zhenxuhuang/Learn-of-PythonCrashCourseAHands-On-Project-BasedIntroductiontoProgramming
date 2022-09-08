# Python编程：从入门到实践
# 第7章 用户输入和while循环
# 7.3
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response
