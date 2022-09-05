# Python编程：从入门到实践
# 第5章 if语句
# 5.2
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")