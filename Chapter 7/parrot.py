"""
Python编程：从入门到实践
第7章 用户输入和while循环

7.1
"""


message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
activate = True
while activate:
    message = input(prompt)
    if message == 'quit':
        activate = False
    else:
        print(message)